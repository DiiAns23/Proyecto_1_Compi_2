from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Length(Funcion):

    def __init__(self, ide, params, inst, fila, columna):
        super().__init__(ide, params, inst, fila, columna)
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("length##Param1")
        if simbolo == None: 
            return Excepcion("Semantico", "Sin parametro en length", self.fila, self.colum)
        print(simbolo.getTipo())
        if simbolo.getTipo() != TIPO.STRING and simbolo.getTipo() != TIPO.ARRAY:
            return Excepcion("Semantico", "length recibe solo expresiones de tipo string o array", self.fila, self.colum)
        
        self.tipo = TIPO.ENTERO
        return len(simbolo.getValor())