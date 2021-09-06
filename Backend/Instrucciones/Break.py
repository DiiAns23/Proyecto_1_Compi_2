from Abstrac.Instruccion import Instruccion

class Break(Instruccion):

    def __init__(self, fila, columna):
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        return self