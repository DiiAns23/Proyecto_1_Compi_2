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

        if self.inst == "println":
            tree.updateConsola(value)
        else:
            tree.updateConsola2(value)
        return None