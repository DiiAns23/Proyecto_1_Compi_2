from Abstrac.Instruccion import Instruccion

class Continue(Instruccion):

    def __init__(self, fila, columna):
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        return self