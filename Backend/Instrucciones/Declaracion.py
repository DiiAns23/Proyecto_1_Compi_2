from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class Declaracion(Instruccion):
    def __init__(self, ide, fila, columna, tipo = None,valor = None):
        self.id = ide
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        if self.tipo != TIPO.ARRAY and self.tipo != TIPO.STRUCT:
            if self.valor != None:
                if self.tipo!=None:
                    value = self.valor.interpretar(tree, table)
                    print("Si entra aqui :3")
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
        elif self.tipo == TIPO.ARRAY:
            if self.valor != None:
                lista = []
                for valores in self.valor:
                    value = valores.interpretar(tree, table)
                    if isinstance(value, Excepcion): return value
                    simbolo = Simbolo("", valores.getTipo(), valores.fila, valores.colum, value)
                    lista.append(simbolo)
                array = Simbolo(self.id, TIPO.ARRAY, self.fila, self.colum, lista)
                result = table.setTabla(array)
                if result == "Asignacion":
                    table.updateTabla(array)
                return None
            
        elif self.tipo == TIPO.STRUCT:
            if self.valor:
                dict = {}
                for valores in self.valor:
                    simbolo = Simbolo("", valores.tipo, self.fila, self.colum, valores.valor )
                    dict[str(valores.id)] = simbolo
                print("Diccionario", str(dict))
                print("Nombre: ", dict['nombre'].getValor())