import re
import ply.yacc as yacc
import ply.lex as lex
from TablaSimbolos.Arbol import Arbol
from Analizador_Lexico import tokens
from Analizador_Lexico import lexer
from Analizador_Lexico import find_column
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos



# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right','UNOT'),
    ('left', 'IGUALDAD', 'DIFERENTE'),
    ('nonassoc', 'MENOR', 'MAYOR'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV'),
    ('right','UMENOS'),
    ('left','PARI', 'PARD'),
    )

from Abstrac.Instruccion import Instruccion
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Tipo import TIPO, OperadorAritmetico
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
                    | condicional_if PTCOMA
                    | loop_while PTCOMA
                    | loop_for PTCOMA'''
    t[0] = t[1]

def p_imprimir(t):
    '''imprimir : RPRINT PARI expresion PARD'''
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_tipo(t):
    '''declaracion_instr : ID IGUAL expresion DPUNTOS DPUNTOS tipo'''
    t[0] = print("Variable: " + str(t[1]) + " Valor: " + str(t[3])+ " Tipo: " + str(t[6]))

def p_declaracion_non_tipo(t):
    '''declaracion_instr : ID IGUAL expresion'''
    t[0] = print("Variable: " + str(t[1]) + " Valor: " + str(t[3]))

def p_tipof_1(t):
    '''tipo_f : RPARSE
                | RTRUNC
                | RFLOATF
                | RSTRINGF
                | RTYPEOF'''
    t[0] = t[1]

def p_functions_natives(t):
    '''llamada_function : tipo_f PARI expresion PARD'''
    t[0] = print("Funcion nativa: " + t[1] + " Expresion: "+ str(t[3]))

def p_llamada_function_1(t):
    'llamada_function : ID PARI parametros PARD'
    t[0] = print("Llamada de Funcion: " + t[1] + " Parametros: " + str(t[3]))

def p_llamada_function_2(t):
    'llamada_function : ID PARI PARD'
    t[0] = print("Llamada de la funcion: " + t[1])

def p_declaracion_function_1(t):
    '''declaracion_function : RFUNCTION ID PARI parametros PARD instrucciones REND'''
    t[0] = print("Funcion: " + t[2] + " Parametros: " + str(t[4]))

def p_condicional_if_1(t):
    '''condicional_if : RIF expresion instrucciones REND'''
    t[0] = print("Condicional If: " + str(t[2]))

def p_condicional_if_2(t):
    '''condicional_if : RIF expresion instrucciones RELSE instrucciones REND'''
    t[0] = print("Condicional if-else")

def p_loop_while_1(t):
    '''loop_while : RWHILE expresion instrucciones REND'''
    t[0] = print("Loop While: " + str(t[2]))

def p_loop_for_1(t):
    '''loop_for : RFOR expresion RIN rango instrucciones REND'''
    t[0] = print("Loop For: " + str(t[4]))

def p_rango(t):
    'rango : ENTERO DPUNTOS ENTERO'
    t[0] = [t[1], t[3]]
    
def p_params(t):
    'parametros : parametros COMA expresion'
    t[1].append(t[3])
    t[0] = t[1]

def p_params2(t):
    'parametros : expresion'
    t[0] = [t[1]]

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
    elif t[2] == '*': 
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '>': t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '<=': t[0] = t[1] >= t[3]
    elif t[2] == '||': t[0] = t[1] or t[3]
    elif t[2] == '&&': t[0] = t[1] and t[3]

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                    | NOT expresion %prec UNOT'''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UME, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!': t[0] = not t[2]

def p_expresion_agrupacion(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = "identificador"
    # Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

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
    
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

input = ''

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
# print(entrada)
# print("")
# print("ARCHIVO DE SALIDA")
# instrucciones = parse(entrada)
# ast = Arbol(instrucciones)
# TsgGlobal = Tabla_Simbolos()
# ast.setTSglobal(TsgGlobal)
# for error in errores:
#     ast.getExcepciones().append(error)
#     ast.updateConsola(error.toString())
# for instruccion in ast.getInst():
#     value = instruccion.interpretar(ast,TsgGlobal)
    