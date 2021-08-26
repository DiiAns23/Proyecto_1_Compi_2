from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion
from math import *

class Seno(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("sin##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en sin", self.fila, self.colum)
        if simbolo.getTipo() != TIPO.ENTERO and simbolo.getTipo() != TIPO.FLOAT:
            return Excepcion("Semantico", "sin recibe solo expresiones de tipo Int64 o Float", self.fila, self.colum)

        self.tipo = TIPO.FLOAT
        
        return sin(simbolo.getValor())