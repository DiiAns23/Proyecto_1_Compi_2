from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Asignacion_Struct(Instruccion):
    def __init__(self, ide, fila, columna, parametros, valor):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.parametros = parametros
        self.valor = valor
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        struct = table.getTabla(self.ide)
        if struct == None:
            return Excepcion("Semantico", "struct no encontrado", self.fila, self.fila)
        if struct.mutable == True:
            value = self.valor.interpretar(tree, table)
            if isinstance(value, Excepcion): return value
            
            claves = []
            for params in self.parametros:
                claves.append(str(params))
            simbolo = Simbolo(self.ide, self.valor.tipo, self.fila, self.colum, value)
            result = table.updateStruct(simbolo, claves)
            if isinstance(result, Excepcion): return result
        else:
            return Excepcion("Semantico", "No se pueden realizar cambios", self.fila, self.colum)
        
        


    