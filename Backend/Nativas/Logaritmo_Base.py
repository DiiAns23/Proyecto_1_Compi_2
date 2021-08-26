from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion
from math import *

class Logaritmo_Base(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("log##Param1")
        valor = table.getTabla("log##Param2")
        if simbolo == None or valor == None: 
            return Excepcion("Semantico", "Sin parametro en log", self.fila, self.colum)
        if (simbolo.getTipo() != TIPO.ENTERO and simbolo.getTipo() != TIPO.FLOAT) or (valor.getTipo() != TIPO.ENTERO and valor.getTipo() != TIPO.FLOAT):
            return Excepcion("Semantico", "log recibe solo expresiones de tipo Int64 o Float", self.fila, self.colum)

        self.tipo = TIPO.FLOAT
        
        return log(valor.getValor(),simbolo.getValor())