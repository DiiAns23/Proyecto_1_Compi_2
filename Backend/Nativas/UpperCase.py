from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class UpperCase(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("uppercase##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en uppercase", self.fila, self.colum)
        if simbolo.getTipo() != TIPO.STRING:
            return Excepcion("Semantico", "uppercase recibe solo expresiones de tipo String", self.fila, self.colum)
        
        self.tipo = simbolo.getTipo()
        return simbolo.getValor().upper()