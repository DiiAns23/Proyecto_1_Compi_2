from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Typeof(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeof##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en typeof", self.fila, self.colum)
        self.tipo = simbolo.getTipo()
        if self.tipo == TIPO.ENTERO:
            return "Int64"
        if self.tipo == TIPO.FLOAT:
            return "Float64"
        if self.tipo == TIPO.STRING:
            return "String"
        if self.tipo == TIPO.CHAR:
            return "Char"
        if self.tipo == TIPO.ARRAY:
            return "Array"
        if self.tipo == TIPO.NULO:
            return "Null"
        if self.tipo == TIPO.BOOL:
            return "Bool"
        if self.tipo == TIPO.STRUCT:
            return "Struct"