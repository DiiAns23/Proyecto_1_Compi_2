from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Stringg(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
        self.tipo = TIPO.STRING
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("string##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en trunc", self.fila, self.colum)
        return str(simbolo.getValor())