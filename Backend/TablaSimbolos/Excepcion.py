class Excepcion:
    def __init__(self, tipo, desc, fila, column):
        self.tipo = tipo
        self.desc = desc
        self.fila = fila
        self.column = column
    
    def toString(self):
        return self.tipo + " - " + self.desc + " [" + str(self.fila) + ", " + str(self.column) + "]"
        