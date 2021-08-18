from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo

class Declaracion(Instruccion):
    def __init__(self, ide, fila, columna, valor = None):
        self.id = ide
        self.valor = valor
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        if self.valor != None:
            value = self.valor.interpretar(tree, table)
            if isinstance(value, Excepcion): return value
            simbolo = Simbolo(str(self.id), self.valor.tipo, self.fila, self.colum, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
        else:
            value = "nothing"
            simbolo = Simbolo(str(self.id), TIPO.NULO, self.fila, self.colum, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
