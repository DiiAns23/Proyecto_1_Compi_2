import re
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class If(Instruccion):
    def __init__(self, condicion, bloqueIf, bloqueElse, bloqueElif, fila, columna):
        self.condicion = condicion
        self.bloqueIf = bloqueIf
        self.bloqueElse = bloqueElse
        self.bloqueElif = bloqueElif
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOL:
            if bool(condicion) is True:
                entorno = Tabla_Simbolos(table)
                for instruccion in self.bloqueIf:
                    result = instruccion.interpretar(tree, entorno)
                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result, Return): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Continue):return result
            else:
                if self.bloqueElse != None:
                    entorno = Tabla_Simbolos(table)
                    for instruccion in self.bloqueElse:
                        result = instruccion.interpretar(tree, entorno)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Return): return result
                        if isinstance(result, Break): return result
                        if isinstance(result, Continue):return result
                elif self.bloqueElif != None:
                    result = self.bloqueElif.interpretar(tree,table)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result, Return): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Continue):return result

