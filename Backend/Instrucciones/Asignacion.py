from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo

class Asignacion(Instruccion):

    def __init__(self,ide, indices, fila, columna, valor = None):
        self.ide = ide
        self.indices = indices
        self.valor = valor
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.ARRAY
    
    def interpretar(self, tree, table):
        if self.valor != None:
            value = self.valor.interpretar(tree,table)
            if isinstance(value, Excepcion): return value
            valores = table.getArray(str(self.ide))
            if isinstance(valores, Excepcion): return valores
            for x in range (0,len(self.indices)):
                try:
                    indice = self.indices[x].interpretar(tree,table)
                    if isinstance(indice, Excepcion): return indice
                    if str(indice) != str(0):
                        indice = indice - 1
                        valores[indice] = value
                    else:
                        return Excepcion("Semantico", "No se ha encontrado el indice ["+str(indice)+"] ", self.fila, self.colum)
                except:
                    return Excepcion("Semantico", "No se ha encontrado el indice ["+str(indice+1)+"] ", self.fila, self.colum)
            simbolo = Simbolo(self.ide, TIPO.ARRAY,self.fila, self.colum, valores)
            result = table.setTabla(simbolo)
            if result == "Asignacion":
                table.updateTabla(simbolo)
            return None

    def cambiarValores(self, lista, indice):
        
        ''