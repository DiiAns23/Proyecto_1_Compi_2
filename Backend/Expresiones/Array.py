from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Array(Instruccion):
    def __init__(self, ide, fila, columna, tipo, indice = None, rango = None):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.tipo = tipo
        self.indices = indice
        self.rango = rango
        self.referencia = 0

    def interpretar(self, tree, table):
        if self.ide:
            simbolo = table.getTabla(self.ide)
            if simbolo == None:
                return Excepcion("Semantico", "Variable no encontrada", self.fila, self.colum)
            if self.rango == None:
                if self.indices:
                    valores = simbolo.getValor()
                    indices = []
                    for indice in self.indices:
                        index = indice.interpretar(tree, table)
                        if int(index) > 0:
                            indices.append(index)
                        else:
                            return Excepcion("Semantico", "Indice fuera de rango", self.fila, self.colum)
                    valores = self.getValores(valores, indices)
                    return valores
                    # return None
                else:
                    values = simbolo.getValor()
                    valores = []
                    for value in values:
                        simbolo = Simbolo("", value.getTipo(), self.fila, self.colum, value.getValor())
                        valores.append(simbolo) 
                    return valores

            else:
                init = self.rango[0].interpretar(tree,table)
                if isinstance(init, Excepcion): return init
                fin = self.rango[1].interpretar(tree, table)
                if isinstance(fin, Excepcion): return fin
                if self.rango[0].tipo != TIPO.ENTERO or self.rango[1].tipo != TIPO.ENTERO:
                    return Excepcion("Semantico", "Solo se acepta tipo Int64", self.fila, self.colum)
                values = simbolo.getValor()
                valores = []
                for i in range(init, fin + 1):
                    try:
                        if int(i) > 0:
                            simbolo = Simbolo("", values[i-1].getTipo(), self.fila, self.colum, values[i-1].getValor())
                            valores.append(simbolo)
                        else:
                            return Excepcion("Semantico", "Indices fuera de rango", self.fila, self.colum)
                    except:
                        return Excepcion("Semantico", "Indices fuera de rango", self.fila, self.colum)

                return valores
        
        else:
            valores = []
            for value in self.rango:
                x = value.interpretar(tree, table)
                if isinstance(x, Excepcion): return x
                simbolo = Simbolo("", value.tipo, self.fila, self.colum, x)
                valores.append(simbolo)
            return valores

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide
    
    def getValores(self,anterior, indices):
        actual = anterior
        for indice in indices:
            try:
                self.tipo = actual[int(indice)-1].getTipo()
                actual = actual[int(indice)-1].getValor()
            except:
                return Excepcion("Semantico", "Indices fuera de rango", self.fila, self.colum)
        return actual 
        
    def copyValues(self, anterior):
        actual = []
        for x in anterior:
            a = x.getValor()
            if isinstance(a, List):
                value = self.copyValues(a)
                simbolo = Simbolo("", TIPO.ARRAY, self.fila, self.colum, value)
                actual.append(simbolo)
            else:
                simbolo = Simbolo("", x.getTipo(), self.fila, self.colum, x.getValor())
                actual.append(simbolo)
        return actual
    