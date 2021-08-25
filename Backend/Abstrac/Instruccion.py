from abc import ABC, abstractmethod

class Instruccion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.colum = columna
        super().__init__()
    
    @abstractmethod
    def interpretar(self, tree, table):
        pass