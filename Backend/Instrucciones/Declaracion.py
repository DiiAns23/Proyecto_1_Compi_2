from Expresiones.Identificador import Identificador
from Expresiones.Array import Array
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo

class Declaracion(Instruccion):
    def __init__(self, ide, fila, columna, tipo = None,valor = None):
        self.id = ide
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        if self.tipo != TIPO.ARRAY:
            if self.valor != None:
                if self.tipo!=None:
                    value = self.valor.interpretar(tree, table)
                    if isinstance(value, Excepcion): return value
                    if str(self.tipo) == str(self.valor.tipo):
                        simbolo = Simbolo(str(self.id), self.valor.tipo, self.fila, self.colum, value)
                        result = table.setTabla(simbolo)
                        if result == "Asignacion":
                            table.updateTabla(simbolo)
                        return None
                    else:
                        result = Excepcion("Semantico", "Error tipos: "+str(self.valor.tipo) +" no coincide con "+ str(self.tipo), self.fila, self.colum)
                        return result
                else:
                    value = self.valor.interpretar(tree, table)
                    if isinstance(value, Excepcion): return value
                    simbolo = Simbolo(str(self.id), self.valor.tipo, self.fila, self.colum, value)
                    result = table.setTabla(simbolo)
                    if result == "Asignacion":
                        table.updateTabla(simbolo)
                    return None
            else:
                value = "nothing"
                simbolo = Simbolo(str(self.id), TIPO.NULO, self.fila, self.colum, value)
                result = table.setTabla(simbolo)
                if isinstance(result, Excepcion): return result
                return None
        else:
            if self.valor != None:
                lista = []
                for valores in self.valor:
                    value = valores.interpretar(tree, table)
                    if isinstance(value, Excepcion): return value
                    lista.append(value)
                array = Simbolo(self.id, TIPO.ARRAY, self.fila, self.colum, lista)
                result = table.setTabla(array)
                if result == "Asignacion":
                    table.updateTabla(array)
                return None
            
