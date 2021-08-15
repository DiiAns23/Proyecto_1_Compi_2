import ply.lex as lex
import ply.yacc as yacc

errores = []

reserved = {
    'print' : 'RPRINT'
}

tokens  = [
    'PTCOMA',
    'PARI',
    'PARD',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'IGUAL',
    'IGUALDAD',
    'DIFERENTE',
    'MAYOR',
    'MENOR',
    'MAYORI',
    'MENORI',
    'OR',
    'AND',
    'NOT',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CHAR',
    'ID'
]+ list(reserved.values())

# Tokens
t_RPRINT        = r'print'
t_PTCOMA        = r';'
t_PARI          = r'\('
t_PARD          = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'\/'
t_IGUAL         = r'='
t_IGUALDAD      = r'=='
t_DIFERENTE     = r'!='
t_MAYOR         = r'>'
t_MENOR         = r'<'
t_MAYORI        = r'>='
t_MENORI        = r'<='
t_OR            = r'\|\|'
t_AND           = r'&&'
t_NOT           = r'!'


#Decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

#Entero
def t_ENTERO(n):
    r'\d+'
    try:
        if(n.value != None):
            n.value = int(n.value)
        else:
            n.value = 'nothing'
    except ValueError:
        print("Valor del entero demasiado grande %d", n.value)
        n.value = 0
    return n

#Char
def t_CHAR(n):
    r'\'(\\\'|\\"|\\t|\\n|\\\\|[^\'\\])\''
    n.value = n.value[1:-1] #Se remueven las comillas de la entrada
    n.value = n.value.replace('\\t','\t')
    n.value = n.value.replace('\\n','\n')
    n.value = n.value.replace('\\"','\"')
    n.value = n.value.replace("\\'","\'")
    n.value = n.value.replace('\\\\','\\')
    return n

#CADENA
def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')# Check for reserved words
     return t

#Caracteres Ignorados


#Comentario de Una Linea
def t_Com_Simple(n):
    r'\#.*\n'
    # n.lexer.lineno += 1

#Comentario Multilinea
def t_Com_Multiple(n):
    r'\#\*(.|\n)*?\*\#'
    # n.lexer.lineno += 1

def t_newline(t):
    r'\n+'
    #t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = " \t"

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



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

# Definicion de la Gramatica
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instrucciones_evaluar(t):
    '''instruccion : RPRINT PARI expresion PARD PTCOMA
                    '''
    print(str(t[3]))

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIV expresion
                  | expresion IGUALDAD expresion
                  | expresion DIFERENTE expresion
                  | expresion MAYOR expresion
                  | expresion MENOR expresion
                  | expresion MAYORI expresion
                  | expresion MENORI expresion
                  | expresion OR expresion
                  | expresion AND expresion
                  '''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
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
    if t[1] == '-': t[0] = t[2]
    elif t[1] == '!': t[0] = t[2]

def p_expresion_agrupacion(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = "identificador"
    # Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL
                    | CHAR
                    | CADENA'''
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print("ARCHIVO DE ENTRADA:")
print(input)
print("")
print("ARCHIVO DE SALIDA:")
parser.parse(input)
print("")

# def parse(input):
#     cad = parser.parse(input)
#     return cad
