from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Pop(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
    
    def interpretar(self, tree, table):
        variable = table.getTabla("pop##Param1")
        if variable == None:
            return Excepcion("Semantico", "Faltan parametros en pop ", self.fila, self.colum)
        values = variable.getValor()
        return values.pop().getValor()
