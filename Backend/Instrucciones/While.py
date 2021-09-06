from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion

class While(Instruccion):

    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        while True:
            bandera = False
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion
            if self.condicion.tipo == TIPO.BOOL:
                if bool(condicion) == True:
                    for instruccion in self.instrucciones:
                        entorno = Tabla_Simbolos(table)
                        value = instruccion.interpretar(tree, entorno)
                        if isinstance(value, Excepcion):
                            tree.getExcepciones().append(value)
                            tree.updateConsola(value.toString())
                        if isinstance(value, Break): 
                            return None
                        if isinstance(value, Return): return value
                        if isinstance(value, Continue): 
                            bandera = True
                            break
                else: 
                    break
            else:
                return Excepcion("Semantico", "Condicion no valida en el While", self.fila, self.colum)
            if bandera:
                continue
            