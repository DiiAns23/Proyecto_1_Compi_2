import ply.lex as lex

errores = []

reserved = {
    'print'     :   'RPRINT',
    'Int64'     :   'RINT',
    'Float64'   :   'RFLOAT',
    'Bool'      :   'RBOOL',
    'Char'      :   'RCHAR',
    'String'    :   'RSTRING',
    'function'  :   'RFUNCTION',
    'end'       :   'REND',
    'parse'     :   'RPARSE',
    'trunc'     :   'RTRUNC',
    'float'     :   'RFLOATF',
    'string'    :   'RSTRINGF',
    'typeof'    :   'RTYPEOF',
    'push'      :   'RPUSH',
    'pop'       :   'RPOP',
    'length'    :   'RLENGTH',
    'if'        :   'RIF',
    'else'      :   'RELSE',
    'elseif'    :   'RELSEIF',
    'while'     :   'RWHILE',
    'for'       :   'RFOR',
    'in'        :   'RIN'
}

tokens  = [
    'COMA',
    'PTCOMA',
    'DPUNTOS',
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
t_COMA          = r','
t_PTCOMA        = r';'
t_DPUNTOS       = r':'
t_PARI          = r'\('
t_PARD          = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'\/'
t_IGUALDAD      = r'=='
t_IGUAL         = r'\='
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

#Cadena
def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

#Identificador
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')# Check for reserved words
     return t

#Comentario de Una Linea
def t_Com_Simple(t):
    r'\#.*\n'
    t.lexer.lineno += 1

#Comentario Multilinea
def t_Com_Multiple(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += 1

#Nueva Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = " \t"

#Error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Crear archivo lexico
lexer = lex.lex()