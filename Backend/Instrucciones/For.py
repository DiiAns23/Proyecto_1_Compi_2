from typing import List
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from TablaSimbolos.Simbolo import Simbolo
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion

class For(Instruccion):

    def __init__(self, inicio, rango, instrucciones,  fila, columna):
        self.inicio = inicio
        self.rango = rango
        self.instrucciones = instrucciones
        self.fila = fila
        self.colum = columna

    def interpretar(self, tree, table):
        inicio = self.inicio.interpretar(tree, table)
        if isinstance(inicio, Excepcion): return inicio
        if len(self.rango) == 1:
            if not isinstance(self.rango[0], List):
                value = self.rango[0].interpretar(tree, table)
                if isinstance(value, Excepcion): return value
                if self.rango[0].getTipo() == TIPO.STRING:
                    values = list(value)
                    result = self.Ciclo(tree, table, inicio, values)
                    return result
                elif self.rango[0].getTipo() == TIPO.ARRAY:
                    rango = self.rango[0].interpretar(tree, table)
                    if isinstance(rango, Excepcion): return rango
                    values = []
                    for x in rango:
                        val = x.getValor()
                        if isinstance(val, Excepcion): return val
                        values.append(val)
                    result = self.Ciclo(tree, table, inicio, values)
                    return result
                return Excepcion("Semantico", "No se ha definido un rango en el ciclo for", self.fila, self.colum)
            else:
                self.rango = self.rango[0]
                values = []
                for value in self.rango:
                    val = value.interpretar(tree, table)
                    if isinstance(val, Excepcion): return val
                    values.append(val)
                result = self.Ciclo(tree, table, inicio, values)
                return result
            
        else:
            self.inicio.valor = self.rango[1]
            inicio = self.inicio.interpretar(tree, table)
            if isinstance(inicio, Excepcion): return inicio
            init = self.rango[0].interpretar(tree, table)
            if isinstance(init, Excepcion): return init
            fin = self.rango[1].interpretar(tree, table)
            if isinstance(fin, Excepcion): return fin
            if self.rango[0].tipo == TIPO.ENTERO and self.rango[1].tipo == TIPO.ENTERO:
                for x in range(init, fin + 1):
                    entorno = Tabla_Simbolos(table) 
                    simbolo = Simbolo(self.inicio.id,TIPO.ENTERO, self.fila, self.colum, x)
                    result = entorno.setTabla(simbolo)
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, entorno)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Return): return result
                        if isinstance(result, Break): return None
                        if isinstance(result, Continue): break
            else:
                return Excepcion("Semantico", "Error en el rango del ciclo for", self.fila, self.colum)
                    
    def Ciclo(self,tree, table, inicio, values):
        for x in values:
            entorno = Tabla_Simbolos(table)
            simbolo = Simbolo(self.inicio.id, TIPO.ARRAY, self.fila, self.colum, x)
            result = entorno.setTabla(simbolo)
            for instruccion in self.instrucciones:
                result = instruccion.interpretar(tree, entorno)
                if isinstance(result, Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Return): return result
                if isinstance(result, Break): return None
                if isinstance(result, Continue): break
        return None

        