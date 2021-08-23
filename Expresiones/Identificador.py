from TablaSimbolos import Excepcion
from Abstrac.Instruccion import Instruccion

class Identificador(Instruccion):
    def __init__(self, ide, fila, columna):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.ide)
        if simbolo == None:
            return Excepcion("Semantico", "Variable: " + self.ide + " no encontrada", self.fila, self.colum)
        
        self.tipo = simbolo.getTipo()

        return simbolo.getValor()
    
    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide