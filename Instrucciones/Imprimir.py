from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, colum):
        self.exp = expresion
        self.fila = fila
        self.colum = colum
    
    def interpretar(self, tree, tabla):
        value = self.exp.interpretar(tree, tabla)

        if isinstance(value, Excepcion):
            print(value)
            return value
        if self.exp.tipo == TIPO.ARRAY:
            return Excepcion("Semantico", "No se puede imprimir un arreglo completo", self.fila, self.colum)
        print(value)
        tree.updateConsola(value)
        return None