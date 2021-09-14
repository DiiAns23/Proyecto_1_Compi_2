from Instrucciones.Asignacion import Asignacion
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Excepcion import Excepcion

class Funcion(Instruccion):
    def __init__(self, ide, params, inst, fila, columna):
        self.ide = ide
        self.params = params
        self.inst = inst
        self.fila = fila
        self.colum = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        entorno = Tabla_Simbolos(table)
        for ins in self.inst:
            value = ""
            if isinstance(ins, Asignacion) or isinstance(ins, Declaracion):
                value = ins.interpretar(tree, table)
            else:
                value = ins.interpretar(tree, entorno)
            if isinstance(value, Excepcion): 
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.value
            if isinstance(value, Break):
                error  = Excepcion("Semantico", "Break fuera de ciclo", ins.fila, ins.colum)
                tree.getExcepciones().append(error)
                tree.updateConsola(error.toString())
        return None
        
        