class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = []
        self.excepciones = []
        self.consola = ""
        self.tsglobal = None
    
    def getInst(self):
        return self.instrucciones
    
    def setInst(self, instrucciones):
        self.instrucciones = instrucciones
    
    def getFunciones(self):
        return self.funciones
    
    def setFunciones(self, funciones):
        self.funciones.append(funciones)
    
    def getExcepciones(self):
        return self.excepciones
    
    def setExcepciones(self, excep):
        self.excepciones = excep
    
    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola
    
    def updateConsola(self, cadena):
        self.consola += str(cadena) + '\n'
    
    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal