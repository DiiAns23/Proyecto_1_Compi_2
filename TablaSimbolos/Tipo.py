from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    FLOAT = 2
    BOOL = 3
    CHAR = 4
    STRING = 5
    NULO = 6
    ARRAY = 7

class OperadorAritmetico(Enum):
    MAS = 1
    MEN = 2
    POR = 3
    DIV = 4
    POT = 5
    MOD = 6
    UME = 7

class OperadorRelacional(Enum):
    MENOR = 1
    MAYOR = 2
    MENORI = 3
    MAYORI = 5
    IGUALDAD = 6
    DIFERENTE = 7

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3
