from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import OperadorAritmetico, TIPO
from Abstrac.Instruccion import Instruccion

class Aritmetica(Instruccion):
    def __init__(self, op, opi, opd, fila, columna):
        self.op = op
        self.opi = opi
        self.opd = opd
        self.fila = fila
        self.colum = columna
        self.tipo = None

    def interpretar(self, tree, table):
        izq = self.opi.interpretar(tree,table)
        if isinstance(izq, Excepcion): return izq
        if self.opd != None:
            der = self.opd.interpretar(tree, table)
            if isinstance(der,Excepcion): return der
        # ----------------------------------------------- SUMA -------------------------------------- #
        if self.op == OperadorAritmetico.MAS:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.getValor(self.opi.tipo, izq) + self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) + self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) + self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) + self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la suma + ", self.fila, self.colum)

        # ----------------------------------------------- RESTA -------------------------------------- #
        elif self.op == OperadorAritmetico.MEN:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.getValor(self.opi.tipo, izq) - self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) - self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) - self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) - self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la resta - ", self.fila, self.colum)

        # ----------------------------------------------- POR -------------------------------------- #
        elif self.op == OperadorAritmetico.POR:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.getValor(self.opi.tipo, izq) * self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) * self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) * self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) * self.getValor(self.opd.tipo, der)
            elif self.opi.tipo == TIPO.STRING and self.opd.tipo == TIPO.STRING:
                self.tipo = TIPO.STRING
                return self.getValor(self.opi.tipo, izq) + self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la multiplicacion * ", self.fila, self.colum)

        # ----------------------------------------------- DIV -------------------------------------- #
        elif self.op == OperadorAritmetico.DIV:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) / self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) / self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) / self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) / self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la division / ", self.fila, self.colum)

        # ----------------------------------------------- POT -------------------------------------- #
        elif self.op == OperadorAritmetico.POT:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.getValor(self.opi.tipo, izq) ** self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) ** self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) ** self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) ** self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.STRING and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.STRING
                return self.getValor(self.opi.tipo, izq) * self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en la potencia ^ ", self.fila, self.colum)
        
        # ----------------------------------------------- MOD -------------------------------------- #
        elif self.op == OperadorAritmetico.MOD:
            if self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.getValor(self.opi.tipo, izq) % self.getValor(self.opd.tipo, der)
                
            elif self.opi.tipo == TIPO.ENTERO and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) % self.getValor(self.opd.tipo, der)

            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.ENTERO:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) % self.getValor(self.opd.tipo, der)
            
            elif self.opi.tipo == TIPO.FLOAT and self.opd.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return self.getValor(self.opi.tipo, izq) % self.getValor(self.opd.tipo, der)
            return Excepcion("Semantico", "Error en el moduglo % ", self.fila, self.colum)

        # ----------------------------------------------- UME -------------------------------------- #
        elif self.op == OperadorAritmetico.UME:
            if self.opi.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.getValor(self.opi.tipo, izq)
            elif self.opi.tipo == TIPO.FLOAT:
                self.tipo = TIPO.FLOAT
                return - self.getValor(self.opi.tipo, izq)
            return Excepcion("Semantico", "Error en la negacion - unaria", self.fila, self.colum)

        # ----------------------------------------------- SUMA -------------------------------------- #
        if self.op == OperadorAritmetico.COMA:
            self.tipo = TIPO.STRING
            return str(self.getValor(self.opi.tipo, izq)) + str(self.getValor(self.opd.tipo, der))

        return Excepcion("Semantico", "Tipo de operacion no especificada", self.fila, self.colum)

    def getValor(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.FLOAT:
            return float(val)
        elif tipo == TIPO.BOOL:
            return bool(val)
        return str(val)
