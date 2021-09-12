from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Push(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
    
    def interpretar(self, tree, table):
        variable = table.getTabla("push##Param1")
        valor = table.getTabla("push##Param2")
        if valor == None or variable == None:
            return Excepcion("Semantico", "Faltan parametros en push! ", self.fila, self.colum)
        
        values = variable.getValor()
        simbolo = Simbolo("", valor.getTipo(), self.fila, self.colum, valor.getValor())
        values.append(simbolo)
        
        return None

        