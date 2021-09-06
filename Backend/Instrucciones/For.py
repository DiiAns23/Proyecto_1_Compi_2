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
               
        if len(self.rango) == 1:
            init = self.rango[1].interpretar(tree, table)
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
                        # result = ""
                        # if isinstance(instruccion,Declaracion):
                        #     result = instruccion.interpretar(tree, table)
                        # else:
                        result = instruccion.interpretar(tree, entorno)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Return): return result
                        if isinstance(result, Break): return None
                        if isinstance(result, Continue): break
            else:
                return Excepcion("Semantico", "Error en el rango del ciclo for", self.fila, self.colum)
                    
                    

                

            

        

        