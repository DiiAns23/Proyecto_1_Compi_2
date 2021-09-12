from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self,inst, expresion, fila, colum):
        self.inst = inst
        self.exp = expresion
        self.fila = fila
        self.colum = colum
    
    def interpretar(self, tree, tabla):
        value = self.exp.interpretar(tree, tabla)
        if isinstance(value, Excepcion):
            return value
        if isinstance(value, List):
            value = self.getValores(value)
            if len(value) == 1:
                value = value[0]

        if self.inst == "println":
            tree.updateConsola(value)
        else:
            tree.updateConsola2(value)
        return None
    
    def getValores(self, anterior):
        actual = []
        for x in anterior:
            a = x.getValor()
            if isinstance(a, List):
                value = self.getValores(a)
                actual.append(value)
            else:
                actual.append(x.getValor())
        return actual
        