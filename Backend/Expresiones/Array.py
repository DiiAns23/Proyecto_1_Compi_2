from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Array(Instruccion):
    def __init__(self, ide, fila, columna, tipo, indice = None):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.tipo = tipo
        self.indices = indice

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.ide)
        if simbolo == None:
            error = "Semantico - Variable o valor no encontrados " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
            return error

        if self.indices:
            valores = simbolo.getValor()
            for indice in self.indices:
                index = indice.interpretar(tree, table)
                if index > 0:
                    try:
                        valores = valores[index-1]
                    except:
                        error = "Semantico - Indice fuera de rango " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
                        return error 
                else:
                    error = "Semantico - Indice fuera de rango " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
                    return error 
        return valores

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide