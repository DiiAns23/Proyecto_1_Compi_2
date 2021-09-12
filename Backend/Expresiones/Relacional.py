from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import OperadorRelacional, TIPO
from Abstrac.Instruccion import Instruccion


class Relacional(Instruccion):
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
        der = self.opd.interpretar(tree,table)
        if isinstance(der, Excepcion): return der

        if self.op == OperadorRelacional.MENOR:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) < self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) < self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) < self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) < self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) < self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la operacion <", self.fila, self.colum)

        elif self.op == OperadorRelacional.MAYOR:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) > self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) > self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) > self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) > self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) > self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la operacion >", self.fila, self.colum)

        elif self.op == OperadorRelacional.MAYORI:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) >= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) >= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) >= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) >= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) >= self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la operacion >=", self.fila, self.colum)

        elif self.op == OperadorRelacional.MENORI:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) <= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) <= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) <= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) <= self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) <= self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la operacion <=", self.fila, self.colum)

        elif self.op == OperadorRelacional.IGUALDAD:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) == self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) == self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) == self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) == self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) == self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.BOOL and self.opi.tipo == TIPO.BOOL:
                return izq == der
            return Excepcion("Semantico", "Error en la operacion ==", self.fila, self.colum)

        elif self.op == OperadorRelacional.DIFERENTE:
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) != self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) != self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.FLOAT and self.opi.tipo == TIPO.FLOAT:
                return self.getValor(self.opi.tipo, izq) != self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.ENTERO and self.opi.tipo == TIPO.ENTERO:
                return self.getValor(self.opi.tipo, izq) != self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.STRING and self.opi.tipo == TIPO.STRING:
                return self.getValor(self.opi.tipo, izq) != self.getValor(self.opd.tipo, der)
            if self.opi.tipo == TIPO.BOOL and self.opi.tipo == TIPO.BOOL:
                return izq != der
            return Excepcion("Semantico", "Error en la operacion !=", self.fila, self.colum)
        
        return Excepcion("Semantico", "Error, tipo de operacion no especificada", self.fila, self.colum)

    def getValor(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.FLOAT:
            return float(val)
        elif tipo == TIPO.BOOL:
            return bool(val)
        return str(val)

    def getTipo(self):
        return self.tipo