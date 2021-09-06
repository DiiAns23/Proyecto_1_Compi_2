from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Float(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
        self.tipo = TIPO.ENTERO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("float##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en float", self.fila, self.colum)
        if simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Solo se aceptan parametros de tipo Int64", self.fila, self.colum)

        return float(simbolo.getValor())