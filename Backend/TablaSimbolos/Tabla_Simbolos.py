from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion

class Tabla_Simbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio es un Diccionario Vacio
        self.anterior = anterior #Al inicio no hay nada
    
    def setTabla(self, simbolo):
        if simbolo.id in self.tabla:
            return "Asignacion"
        else:
            self.tabla[simbolo.id] = simbolo
            return None
    
    def getTabla(self, ide):
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            else:
                tablaActual = tablaActual.anterior
        return None
    
    def updateTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla:
                if tablaActual.tabla[simbolo.id].getTipo() == simbolo.getTipo() or TIPO.NULO:
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None
                return Excepcion("Semantico", "Tipos no coinciden", simbolo.getFila(), simbolo.getColum())
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada", simbolo.getFila(), simbolo.getColum())