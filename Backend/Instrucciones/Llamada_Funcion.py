from typing import Dict, List
from TablaSimbolos.Tipo import TIPO
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
        bandera = True
        result = tree.getFuncion(self.ide)
        if result == None:
            struct = table.getTabla(str(self.ide))
            if struct == None:
                return Excepcion("Semantico", "Funcion o variable no encontrada "+ str(self.ide), self.fila, self.colum)
            else:
                bandera = False
        if bandera == True:
            entorno = Tabla_Simbolos(tree.getTSGlobal())
            if len(result.params) == len(self.params):
                contador = 0
                for expresion in self.params:
                    resultE = expresion.interpretar(tree, table)
                    if isinstance(resultE, Excepcion): return resultE
                    if result.params[contador]["tipo"] == expresion.tipo:
                        simbolo = Simbolo(str(result.params[contador]["ide"]), result.params[contador]['tipo'], self.fila, self.colum, resultE)
                        resultT = entorno.setTablaFuncion(simbolo)
                        if isinstance(resultT, Excepcion): return resultT
                    elif result.params[contador]["tipo"] == "NoTipo":
                        simbolo = Simbolo(str(result.params[contador]["ide"]), expresion.tipo, self.fila, self.colum, resultE)
                        resultT = entorno.setTablaFuncion(simbolo)
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
        else:
            struct = table.getTabla(self.ide)
            dict = struct.getValor()
            dictaux = {}
            list = []
            tipos = []
            for params in self.params:
                resultE = params.interpretar(tree, table)
                if params.tipo == None:
                    simbolo = Simbolo("", TIPO.NULO, self.fila, self.colum, resultE)
                    tipos.append(TIPO.NULO)
                else:
                    simbolo = Simbolo("", params.tipo, self.fila, self.colum, resultE)
                    tipos.append(params.tipo)
                list.append(simbolo)

            self.tipo = TIPO.STRUCT
            for x in dict:
                if dict[x].getTipo() == TIPO.NULO:
                    dictaux[x] = list[0]
                elif dict[x].getTipo() == tipos[0]:
                    dictaux[x] = list[0]
                else:
                    return Excepcion("Semantico", "Tipos no coinciden", self.fila, self.colum)
                list.pop(0)
                tipos.pop(0)
            if len(list) != 0:
                return Excepcion("Semantico", "Demasiados parametros para este struct", self.fila, self.colum)
            aux = {'datos': dictaux, 'mutable': struct.mutable}
            return aux