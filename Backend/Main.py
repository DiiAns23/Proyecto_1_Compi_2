from TablaSimbolos.Tipo import TIPO
from typing import Dict, List
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from flask import Flask, request
import json
from flask.helpers import url_for
from werkzeug.utils import redirect
from Analizador_Sintactico import parse as Analizar
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from Analizador_Lexico import errores, tokens, lexer
from Instrucciones.Funcion import Funcion
from Analizador_Sintactico import agregarNativas as Nativas
from flask_cors import CORS
import sys
sys.setrecursionlimit(10000000)

app = Flask(__name__)
CORS(app)


@app.route('/saludo', methods = ["GET"])
def saludo():
    return "Hola mundo"

@app.route('/prueba', methods = ["POST", "GET"])
def prueba():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        global tmp_val
        tmp_val = entrada["codigo"]
        return redirect(url_for("salida"))
    
@app.route('/salida')
def salida():
    global tmp_val
    global Excepciones
    global Tabla
    Tabla = {}
    instrucciones = Analizar(tmp_val)
    ast = Arbol(instrucciones)
    TsgGlobal = Tabla_Simbolos()
    ast.setTSglobal(TsgGlobal)
    Nativas(ast)
    for error in errores:
        ast.setExcepciones(error)
    for instruccion in ast.getInst():
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion)

    for instruccion in ast.getInst():
        if not (isinstance(instruccion, Funcion)):
            value = instruccion.interpretar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.setExcepciones(value)
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Return fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.setExcepciones(err)
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Break fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.setExcepciones(err)
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Continue fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.setExcepciones(err)
    Excepciones = ast.getExcepciones()
    print("Tabla de Simbolos Global")
    global Simbolos
    Simbolos = ast.getTSGlobal().getTablaG()
    consola = ast.getConsola()
    return json.dumps(consola)

@app.route('/errores')
def getErrores():
    global Excepciones
    aux = []
    for x in Excepciones:
        aux.append(x.toString2())
    return {'valores': aux}

@app.route('/simbolos')
def getTabla():
    global Simbolos
    Dic = []
    for x in Simbolos:
        aux = Simbolos[x].getValor()
        tipo = Simbolos[x].getTipo()
        tipo = getTipo(tipo)
        fila = Simbolos[x].getFila()
        colum = Simbolos[x].getColum()
        if isinstance(aux, List):
            aux = getValores(aux)
            a = []
            a.append(str(x))
            a.append(str(aux))
            a.append('Array')
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
        elif isinstance(aux, Dict):
            aux = getValores2(aux)
            a = []
            a.append(str(x))
            a.append(str(aux))
            a.append('Struct')
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
        else:
            a = []
            a.append(str(x))
            a.append(str(aux))
            a.append(tipo)
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
    return {'valores':Dic}

def getValores(anterior):
    actual = []
    for x in anterior:
        a = x.getValor()
        if isinstance(a, List):
            value = getValores(a)
            actual.append(value)
        elif isinstance(a, Dict):
            value = getValores2(a)
            actual.append(value)
        else:
            actual.append(x.getValor())
    return actual

def getValores2( dict):
    val = "("
    for x in dict:
        a = dict[x].getValor()
        if isinstance(a, List):
            value = getValores(a)
            val += str(value) + ", "
        elif isinstance(a, Dict):
            value = getValores2(a)
            val += str(value) + ", "
        else:
            val += str(dict[x].getValor()) + ", "
    val = val[:-2]  
    val += ")"
    return val

def getTipo(tipo):
    if tipo == TIPO.ENTERO:
        return "Int64"
    if tipo == TIPO.STRING:
        return "String"
    if tipo == TIPO.CHAR:
        return "Char"
    if tipo == TIPO.FLOAT:
        return "Float64"
    if tipo == TIPO.BOOL:
        return "Bool"
    if tipo == TIPO.NULO:
        return "nothing"

if __name__ == '__main__':
    app.run(debug = True, port=5200)