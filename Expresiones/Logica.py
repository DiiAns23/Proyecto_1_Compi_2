from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import OperadorLogico, TIPO
from Abstrac.Instruccion import Instruccion

class Logica(Instruccion):
    def __init__(self, op, opi, opd, fila, colum):
        self.op = op
        self.opi = opi
        self.opd = opd
        self.fila = fila
        self.colum = colum
        self.tipo = TIPO.BOOL

    def interpretar(self, tree, table):
        izq = self.opi.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.opd != None:
            der = self.opd.interpretar(tree,table)
            if isinstance(der, Excepcion): return der
        
        if self.op == OperadorLogico.AND:
            if self.opi.tipo == TIPO.BOOL and self.opd.tipo == TIPO.BOOL:
                return izq and der
            return Excepcion("Semantico", "Error en la operacion &&", self.fila, self.colum)
        elif self.op == OperadorLogico.OR:
            if self.opi.tipo == TIPO.BOOL and self.opd.tipo == TIPO.BOOL:
                return izq or der
            return Excepcion("Semantico", "Error en la operacion ||", self.fila, self.colum)
        elif self.op == OperadorLogico.NOT:
            if self.opi.tipo == TIPO.BOOL:
                return not izq
            return Excepcion("Semantico", "Error en la operacion ||", self.fila, self.colum)
        return Excepcion("Semantico", "Error, operacion no especificada", self.fila, self.colum)
    
    def getValor(self,tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.FLOAT:
            return float(val)
        elif tipo == TIPO.BOOL:
            return bool(val)
        return str(val)