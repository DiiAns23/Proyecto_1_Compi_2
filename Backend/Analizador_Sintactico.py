from Expresiones.Array import Array
from Nativas.Float import Float
from Nativas.Typeof import Typeof
from Nativas.Length import Length
from Nativas.Parse import Parse
from Instrucciones.Asignacion import Asignacion
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.For import For
from Instrucciones.While import While
from Nativas.Tangente import Tangente
from Nativas.Raiz import Raiz
from Nativas.Seno import Seno
from Nativas.Coseno import Coseno
from Nativas.Logaritmo_Base import Logaritmo_Base
from Nativas.Logaritmo import Logaritmo
from Nativas.LowerCase import LoweCase
from Nativas.UpperCase import UpperCase
from Instrucciones.Llamada_Funcion import Llamada_Funcion
from TablaSimbolos.Excepcion import Excepcion
from Instrucciones.Funcion import Funcion
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.If import If
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
import ply.yacc as yacc
import ply.lex as lex
from TablaSimbolos.Arbol import Arbol
from Analizador_Lexico import tokens
from Analizador_Lexico import lexer, errores
from Analizador_Lexico import find_column
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos



# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right','UNOT'),
    ('left', 'IGUALDAD', 'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORI', 'MENORI'),
    ('left','MAS','MENOS','COMA'),
    ('left','POR','DIV', 'MOD'),
    ('left','PARI', 'PARD'),
    ('left','POT'),
    ('right','UMENOS'),
    )

from Abstrac.Instruccion import Instruccion
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Tipo import OperadorRelacional, OperadorLogico, TIPO, OperadorAritmetico
from Instrucciones.Imprimir import Imprimir

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_evaluar(t):
    '''instruccion : imprimir PTCOMA
                    | declaracion_instr PTCOMA
                    | declaracion_function PTCOMA
                    | llamada_function PTCOMA
                    | llamada_function
                    | condicional_if REND PTCOMA
                    | loop_while PTCOMA
                    | loop_for PTCOMA
                    | r_return PTCOMA
                    | r_break  PTCOMA
                    | r_continue PTCOMA
                    | asignacion_array PTCOMA
                    '''
    t[0] = t[1]

def p_imprimir(t):
    '''imprimir : RPRINT PARI expresion PARD
                | RPRINT2 PARI expresion PARD'''
    if t[1] == "print":
        t[0] = Imprimir("print",t[3], t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Imprimir("println",t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_tipo(t):
    '''declaracion_instr : ID IGUAL expresion DPUNTOS DPUNTOS tipo'''
    t[0] = Declaracion(t[1], t.lineno(2), find_column(input, t.slice[2]),t[6], t[3])

def p_declaracion_non_tipo(t):
    '''declaracion_instr : ID IGUAL expresion'''
    t[0] = Declaracion(t[1], t.lineno(2), find_column(input, t.slice[2]),None, t[3])


def p_declaracion_for(t):
    'declaracion_instr  :   ID'
    t[0] = Declaracion(t[1], t.lineno(1), find_column(input, t.slice[1]),None,None)

def p_declaracion_local(t):
    '''declaracion_instr : RLOCAL ID'''
    t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,None)

def p_declaracion_local1(t):
    '''declaracion_instr : RLOCAL ID IGUAL expresion'''
    t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,t[4])

def p_declaracion_global(t):
    'declaracion_instr : RGLOBAL ID'
    t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,None)

def p_declaracion_global1(t):
    '''declaracion_instr : RGLOBAL ID IGUAL expresion'''
    t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,t[4])

def p_declaracion_array(t):
    'declaracion_instr : ID IGUAL CORI parametros_ll CORD'
    t[0] = Declaracion(t[1], t.lineno(1), find_column(input, t.slice[1]), TIPO.ARRAY, t[4])

def p_asignacion_array(t):
    'asignacion_array : ID arrays_1 IGUAL expresion'
    t[0] = Asignacion(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]), t[4])

def p_llamada_function_1(t):
    'llamada_function : ID PARI parametros_ll PARD'
    t[0] = Llamada_Funcion(t[1],t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada_function_2(t):
    'llamada_function : ID PARI PARD'
    t[0] = Llamada_Funcion(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_function_1(t):
    '''declaracion_function : RFUNCTION ID PARI parametros PARD instrucciones REND'''
    t[0] = Funcion(t[2], t[4], t[6], t.lineno(2), find_column(input, t.slice[1]))

def p_declaracion_function_2(t):
    '''declaracion_function : RFUNCTION ID PARI PARD instrucciones REND'''
    t[0] = Funcion(t[2], [], t[5], t.lineno(2), find_column(input, t.slice[1]))

def p_condicional_if_1(t):
    '''condicional_if : RIF expresion instrucciones'''
    t[0] = If(t[2],t[3],None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_2(t):
    '''condicional_if : RIF expresion instrucciones RELSE instrucciones'''
    t[0] = If(t[2],t[3],t[5], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_3(t):
    '''condicional_if : RIF expresion instrucciones RELSE condicional_if'''
    t[0] = If(t[2],t[3],None, t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_while_1(t):
    '''loop_while : RWHILE expresion instrucciones REND'''
    t[0] = While(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_for_1(t):
    '''loop_for : RFOR declaracion_instr RIN rango instrucciones REND'''
    t[0] = For(t[2], t[4], t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_for_2(t):
    '''loop_for : RFOR declaracion_instr RIN expresion instrucciones REND'''
    t[0] = For(t[2], [t[4]], t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_for_3(t):
    '''loop_for : RFOR declaracion_instr RIN CORI parametros_ll CORD instrucciones REND'''
    t[0] = For(t[2], [t[5]], t[7], t.lineno(1), find_column(input, t.slice[1]))


def p_return(t):
    'r_return : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))

def p_break(t):
    'r_break : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

def p_continue(t):
    'r_continue : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

def p_rango(t):
    'rango : expresion DPUNTOS expresion'
    t[0] = [t[1], t[3]]
    
def p_params(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_params1(t):
    'parametros : parametro'
    t[0] = [t[1]]

def p_params2(t):
    'parametro : ID DPUNTOS DPUNTOS tipo'
    t[0] = {'tipo': t[4], 'ide': t[1]}

def p_params3(t):
    'parametro : ID'
    t[0] = {'tipo': "NoTipo" , 'ide':t[1]}

def p_params4(t):
    'parametros_ll : parametros_ll COMA parametro_ll'
    t[1].append(t[3])
    t[0] = t[1]

def p_params5(t):
    'parametros_ll : parametro_ll'
    t[0] = [t[1]]

def p_params6(t):
    '''parametro_ll : expresion
                    | RINT
                    | RFLOAT'''
    if t[1] == "Int64":
        t[0] = Primitivos(TIPO.ENTERO, "Int64", t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == "Float64":
        t[0] = Primitivos(TIPO.FLOAT, "Float", t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = t[1]

def p_params7(t):
    'arrays_1 :  arrays_1 CORI arrays_2 CORD'
    t[1].append(t[3])
    t[0] = t[1]

def p_params8(t):
    'arrays_1 : CORI arrays_2 CORD'
    t[0] = [t[2]]

def p_params9(t):
    'arrays_2 : expresion'
    t[0] = t[1]

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion

                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIV expresion
                  | expresion POT expresion
                  | expresion MOD expresion
                  | expresion IGUALDAD expresion
                  | expresion DIFERENTE expresion
                  | expresion MAYOR expresion
                  | expresion MENOR expresion
                  | expresion MAYORI expresion
                  | expresion MENORI expresion
                  | expresion OR expresion
                  | expresion AND expresion
                  '''
    if t[2] == '+'  : 
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MEN, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == ',':
        t[0] = Aritmetica(OperadorAritmetico.COMA, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%': 
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==': 
        t[0] = Relacional(OperadorRelacional.IGUALDAD, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=': 
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>': 
        t[0] = Relacional(OperadorRelacional.MAYOR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<': 
        t[0] = Relacional(OperadorRelacional.MENOR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=': 
        t[0] = Relacional(OperadorRelacional.MAYORI, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=': 
        t[0] = Relacional(OperadorRelacional.MENORI, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||': 
        t[0] = Logica(OperadorLogico.OR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&': 
        t[0] = Logica(OperadorLogico.AND, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                    | NOT expresion %prec UNOT'''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UME, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!': 
        t[0] = Logica(OperadorLogico.NOT, t[2], None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]), None)

def p_expresion_array(t):
    'expresion : ID arrays_1'
    t[0] = Array(t[1], t.lineno(1), find_column(input, t.slice[1]), TIPO.ARRAY, t[2])

def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos(TIPO.ENTERO, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos(TIPO.FLOAT, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_char(t):
    'expresion : CHAR'
    t[0] = Primitivos(TIPO.CHAR, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos(TIPO.STRING, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_true(t):
    'expresion : RTRUE'
    t[0] = Primitivos(TIPO.BOOL, True, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    'expresion : RFALSE'
    t[0] = Primitivos(TIPO.BOOL, False, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_llam(t):
    'expresion : llamada_function'
    t[0] = t[1]

def p_tipo(t):
    '''tipo : RINT
            | RFLOAT
            | RBOOL
            | RCHAR
            | RSTRING'''
    if t[1] ==  "Int64":
        t[0] = TIPO.ENTERO
    elif t[1] == "Float64":
        t[0] = TIPO.FLOAT
    elif t[1] == "Bool":
        t[0] = TIPO.BOOL
    elif t[1] == "Char":
        t[0] = TIPO.CHAR
    elif t[1] == "String":
        t[0] = TIPO.STRING

def agregarNativas(ast):
    nombre = "uppercase"
    params = [{'tipo':TIPO.STRING, 'ide':'uppercase##Param1'}]
    inst = []
    upper = UpperCase(nombre, params, inst, -1, -1)
    ast.setFunciones(upper)

    nombre = "lowercase"
    params = [{'tipo':TIPO.STRING, 'ide':'lowercase##Param1'}]
    lower = LoweCase(nombre, params, inst, -1, -1)
    ast.setFunciones(lower)

    nombre = "log10"
    params = [{'tipo': 'NoTipo', 'ide': 'log10##Param1'}]
    log_10 = Logaritmo(nombre, params, inst, -1,-1)
    ast.setFunciones(log_10)

    nombre = "log"
    params = [{'tipo': 'NoTipo', 'ide': 'log##Param1'}, {'tipo':'NoTipo', 'ide': 'log##Param2'}]
    log_base = Logaritmo_Base(nombre, params, inst, -1,-1)
    ast.setFunciones(log_base)

    nombre = "sin"
    params = [{'tipo': 'NoTipo', 'ide': 'sin##Param1'}]
    sin = Seno(nombre, params, inst, -1,-1)
    ast.setFunciones(sin)

    nombre = "cos"
    params = [{'tipo': 'NoTipo', 'ide': 'cos##Param1'}]
    cos = Coseno(nombre, params, inst, -1,-1)
    ast.setFunciones(cos)

    nombre = "tan"
    params = [{'tipo': 'NoTipo', 'ide': 'tan##Param1'}]
    tan = Tangente(nombre, params, inst, -1,-1)
    ast.setFunciones(tan)

    nombre = "sqrt"
    params = [{'tipo': 'NoTipo', 'ide': 'sqrt##Param1'}]
    sqrt = Raiz(nombre, params, inst, -1,-1)
    ast.setFunciones(sqrt)

    nombre = "parse"
    params = [{'tipo': 'NoTipo', 'ide': 'parse##Param1'}, {'tipo':TIPO.STRING, 'ide': 'parse##Param2'}]
    parse = Parse(nombre, params, inst, -1,-1)
    ast.setFunciones(parse)

    nombre = "length"
    params = [{'tipo':'NoTipo', 'ide':'length##Param1'}]
    length = Length(nombre, params, inst, -1, -1)
    ast.setFunciones(length)

    nombre = "typeof"
    params = [{'tipo':'NoTipo', 'ide':'typeof##Param1'}]
    typeof = Typeof(nombre, params, inst, -1, -1)
    ast.setFunciones(typeof)

    nombre = "float"
    params = [{'tipo':TIPO.ENTERO, 'ide':'float##Param1'}]
    floats = Float(nombre, params, inst, -1, -1)
    ast.setFunciones(floats)
    
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

input = ''

def getErrores():
    return errores

def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

# f = open("./entrada.txt", "r")
# entrada = f.read()
# print("ARCHIVO DE ENTRADA:")
# print("")
# print(entrada)
# print("")
# print("ARCHIVO DE SALIDA:")
# instrucciones = parse(entrada)
# ast = Arbol(instrucciones)
# TsgGlobal = Tabla_Simbolos()
# ast.setTSglobal(TsgGlobal)

# for error in errores:
#     ast.getExcepciones().append(error)
#     ast.updateConsola(error.toString())

# for instruccion in ast.getInst():
#     if isinstance(instruccion, Funcion):
#         ast.setFunciones(instruccion)
#     if isinstance(instruccion, Declaracion):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())

# for instruccion in ast.getInst():
#     if isinstance(instruccion, Imprimir):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     if isinstance(instruccion, Identificador):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     if isinstance(instruccion, Llamada_Funcion):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     #value = instruccion.interpretar(ast,TsgGlobal)
#     # if isinstance(value, Excepcion):
#     #         ast.getExcepciones().append(value)
#     #         ast.updateConsola(value.toString())
# print(ast.getConsola())