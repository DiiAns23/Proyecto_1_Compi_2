from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class Return(Instruccion):

    def __init__(self,expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila 
        self.colum = columna
        self.value = None
        self.tipo = None
    
    def interpretar(self, tree, table):
        result = self.expresion.interpretar(tree, table)
        if isinstance(result, Excepcion): return result
        self.tipo = self.expresion.tipo
        self.value = result
        return self
