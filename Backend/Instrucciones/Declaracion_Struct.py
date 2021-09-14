from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class Declaracion_Struct(Instruccion):
    def __init__(self, ide, fila, columna, mutable,variables = None):
        self.id = ide
        self.variables = variables
        self.tipo = TIPO.STRUCT
        self.mutable = mutable
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        if self.variables:
            dict = {}
            for variable in self.variables:
                if variable.tipo:
                    simbolo = Simbolo("", variable.tipo, self.fila, self.colum, "nothing" )
                else:
                    simbolo = Simbolo("", TIPO.NULO, self.fila, self.colum, "nothing")
                dict[str(variable.id)] = simbolo
            simbolo = Simbolo(str(self.id), TIPO.STRUCT, self.fila, self.colum, dict)
            table.setTabla(simbolo)
        return None