from TablaSimbolos.Excepcion import Excepcion
import re
import ply.lex as lex

errores = []

reserved = {
    'print'     :   'RPRINT',
    'println'   :   'RPRINT2',
    'Int64'     :   'RINT',
    'Float64'   :   'RFLOAT',
    'Bool'      :   'RBOOL',
    'Char'      :   'RCHAR',
    'String'    :   'RSTRING',
    'function'  :   'RFUNCTION',
    'end'       :   'REND',
    'if'        :   'RIF',
    'else'      :   'RELSE',
    'while'     :   'RWHILE',
    'for'       :   'RFOR',
    'in'        :   'RIN',
    'true'      :   'RTRUE',
    'false'     :   'RFALSE',
    'return'    :   'RRETURN',
    'break'     :   'RBREAK',
    'continue'  :   'RCONTINUE',
    'local'     :   'RLOCAL',
    'global'    :   'RGLOBAL',
    'List'      :   'RLIST'
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
    'POT',
    'MOD',
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
    'ID',
    'CORI',
    'CORD'
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
t_DIV           = r'/'
t_POT           = r'\^'
t_MOD           = r'%'
t_IGUALDAD      = r'=='
t_IGUAL         = r'='
t_DIFERENTE     = r'!='
t_MAYOR         = r'>'
t_MENOR         = r'<'
t_MAYORI        = r'>='
t_MENORI        = r'<='
t_OR            = r'\|\|'
t_AND           = r'&&'
t_NOT           = r'!'
t_CORI          = r'\['
t_CORD          = r'\]'

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
    errores.append(Excepcion("Lexico", "Error Lexico" + t.value[0], t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1

lexer = lex.lex(reflags = re.IGNORECASE)