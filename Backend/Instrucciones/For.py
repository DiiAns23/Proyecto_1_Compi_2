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
        entorno = Tabla_Simbolos(table)        
        if len(self.rango) == 1:
            init = self.rango[1].interpretar(tree, entorno)

        else:
            self.inicio.valor = self.rango[1]
            inicio = self.inicio.interpretar(tree, entorno)
            if isinstance(inicio, Excepcion): return inicio
            init = self.rango[0].interpretar(tree, table)
            fin = self.rango[1].interpretar(tree, table)
            if isinstance(init, Excepcion): return init
            if isinstance(fin, Excepcion): return fin
            simbolo = Simbolo(self.inicio.id,TIPO.ENTERO, self.fila, self.colum, init)
            result = entorno.setTabla(simbolo)
            if result == "Asignacion":
                entorno.updateTabla(simbolo)
            for x in range(init, fin + 1):
                for instruccion in self.instrucciones:
                    result = instruccion.interpretar(tree, entorno)
                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                simbolo = Simbolo(self.inicio.id,TIPO.ENTERO, self.fila, self.colum, x +1)
                result = entorno.setTabla(simbolo)
                if result == "Asignacion":
                    entorno.updateTabla(simbolo)
                
                    

                

            

        

        