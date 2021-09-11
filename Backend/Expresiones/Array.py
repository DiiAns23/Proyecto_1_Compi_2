from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Array(Instruccion):
    def __init__(self, ide, fila, columna, tipo, indice = None):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.tipo = tipo
        self.indices = indice
        self.referencia = 0

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.ide)
        if simbolo == None:
            error = "Semantico - Variable o valor no encontrados " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
            return error

        if self.indices:
            valores = simbolo.getValor()
            indices = []
            for indice in self.indices:
                index = indice.interpretar(tree, table)
                if index > 0:
                    indices.append(index)
                else:
                    error = "Semantico - Indice fuera de rango " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
                    return error
            self.indices = indices
            valores = self.getValores(valores) 
        return valores

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide
    
    def getValores(self,anterior):
        actual = anterior
        for indice in self.indices:
            try:
                self.tipo = actual[indice-1].getTipo()
                actual = actual[indice-1].getValor()
            except:
                actual = "Semantico - Indice fuera de rango " + "[" + str(self.fila) + ", " + str(self.colum) + "]"
        return actual 