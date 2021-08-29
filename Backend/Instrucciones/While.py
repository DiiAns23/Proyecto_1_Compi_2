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
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion
            if self.condicion.tipo == TIPO.BOOL:
                if bool(condicion) == True:
                    #entorno = Tabla_Simbolos(table)
                    for instruccion in self.instrucciones:
                        value = instruccion.interpretar(tree, table)
                        if isinstance(value, Excepcion):
                            tree.getExcepciones().append(value)
                            tree.updateConsola(value.toString())
                else: 
                    break
            else:
                return Excepcion("Semantico", "Condicion no valida en el While", self.fila, self.colum)
