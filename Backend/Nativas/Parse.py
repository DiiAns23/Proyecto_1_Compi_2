from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Parse(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        tipo = table.getTabla("parse##Param1")
        valor = table.getTabla("parse##Param2")
        if tipo == None or valor == None:
            return Excepcion("Semantico", "Faltan parametros en la funcion parse", self.fila, self.colum)
        if (valor.getTipo() != TIPO.STRING):
            return Excepcion("Semantico", "Solo se aceptan parametros String", self.fila, self.colum)
        if tipo.getTipo() == TIPO.ENTERO:
            self.tipo = TIPO.ENTERO
            try:
                ints = int(valor.getValor())
                return ints
            except:
                return Excepcion("Semantico", "No se puede parsear a Int64", self.fila, self.colum)
        elif tipo.getTipo() == TIPO.FLOAT:
            self.tipo = TIPO.FLOAT
            try:
                floats = float(valor.getValor())
                return floats
            except:
                return Excepcion("Semantico", "No se puede parsear a Float64", self.fila, self.colum)
        else:
            return Excepcion("Semantico", "Error en la funcion parse", self.fila, self.colum)
        
        