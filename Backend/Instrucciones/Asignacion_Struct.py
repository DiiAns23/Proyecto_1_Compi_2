from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from typing import List
from Abstrac.Instruccion import Instruccion
from TablaSimbolos.Tipo import TIPO

class Asignacion_Struct(Instruccion):
    def __init__(self, ide, fila, columna, parametros, valor):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.parametros = parametros
        self.valor = valor
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        print("Si entra hasta aqui correctamente :3")
    