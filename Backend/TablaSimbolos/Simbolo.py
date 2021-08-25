class Simbolo:
    def __init__(self, ide, tipo,fila, colum, valor):
        self.id = ide
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.colum = colum
    
    def getID(self):
        return self.id
    
    def setID(self, ide):
        self.id = ide

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor

    def getFila(self):
        return self.fila
    
    def setFila(self, fila):
        self.fila = fila
    
    def getColum(self):
        return self.valor
    
    def setColum(self, colum):
        self.colum = colum
    