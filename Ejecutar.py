from Analizador_Sintactico import parse
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
#Aqui solo ejecuta sin errores :3

f = open("./entrada.txt", "r")
entrada = f.read()
print("ARCHIVO DE ENTRADA:")
print(entrada)
print("")
print("ARCHIVO DE SALIDA")
instrucciones = parse(entrada)
ast = Arbol(instrucciones)
TsgGlobal = Tabla_Simbolos()
ast.setTSglobal(TsgGlobal)
for instruccion in ast.getInst():
    value = instruccion.interpretar(ast,TsgGlobal)