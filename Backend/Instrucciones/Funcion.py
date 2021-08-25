from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion


class Funcion(Instruccion):
    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        entorno = Tabla_Simbolos(table)
        for ins in self.inst:
            value = ins.interpretar(tree, entorno)
            if isinstance(value, Excepcion): 
                tree.getExepciones().append(value)
                tree.updateConsola(value.toString())
        return None
        
        