from TablaSimbolos.Excepcion import Excepcion
from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Identificador(Instruccion):
    def __init__(self, ide, fila, columna, tipo = None):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.tipo = tipo

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.ide)
        if simbolo == None:
            return Excepcion("Semantico", "Variable no encontrada", self.fila, self.colum)
        self.tipo = simbolo.getTipo()
        # if isinstance(simbolo.getValor(), List):
        #     print("Valor retornado: ", str(simbolo.getValor()[0].getTipo()))
        return simbolo.getValor()

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide