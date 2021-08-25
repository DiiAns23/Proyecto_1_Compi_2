from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion

class Llamada_Funcion(Instruccion):
    def __init__(self, ide, params, fila, columna):
        self.ide = ide
        self.params = params
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        result = tree.getFuncion(self.ide)
        if result == None:
            return Excepcion("Semantico", "Funcion no encontrada "+ str(self.ide), self.fila, self.colum)
        entorno = Tabla_Simbolos(tree.getTSGlobal())
        if len(result.params) == len(self.params):
            contador = 0
            for expresion in self.params:
                resultE = expresion.interpretar(tree, table)
                if isinstance(resultE, Excepcion): return resultE
                if result.params[contador]["tipo"] == expresion.tipo:
                    simbolo = Simbolo(str(result.params[contador]["ide"]), result.params[contador]['tipo'], self.fila, self.colum, resultE)
                    resultT = entorno.setTabla(simbolo)
                    if isinstance(resultT, Excepcion): return resultT
                elif result.params[contador]["tipo"] == "NoTipo":
                    simbolo = Simbolo(str(result.params[contador]["ide"]), expresion.tipo, self.fila, self.colum, resultE)
                    resultT = entorno.setTabla(simbolo)
                    if isinstance(resultT, Excepcion): return resultT
                else:
                    return Excepcion("Semantico", "Parametros no coinciden", self.fila, self.colum)
                contador += 1
        else:
            return Excepcion("Semantico", "Parametros incorrectos", self.fila,self.colum)
        
        value = result.interpretar(tree, entorno)
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo
        return value
        