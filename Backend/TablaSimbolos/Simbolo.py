# from Abstrac.Instruccion import Instruccion

class Simbolo():
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
    
    def getValorArray(self, indice):
        if indice:
            try:
                return self.valor[indice]
            except:
                return None
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def setValorArray(self, valor, indice = None):
        if indice:
            try:
                ''
            except:
                ''
        self.valor = valor

    def getFila(self):
        return self.fila
    
    def setFila(self, fila):
        self.fila = fila
    
    def getColum(self):
        return self.colum
    
    def setColum(self, colum):
        self.colum = colum
