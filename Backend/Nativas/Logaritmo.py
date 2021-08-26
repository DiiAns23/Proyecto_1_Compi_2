from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion
from math import *

class Logaritmo(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("log10##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en log10", self.fila, self.colum)
        if simbolo.getTipo() != TIPO.ENTERO and simbolo.getTipo() != TIPO.FLOAT:
            return Excepcion("Semantico", "log10 recibe solo expresiones de tipo Int64 o Float", self.fila, self.colum)

        self.tipo = TIPO.FLOAT
        
        return log10(simbolo.getValor())