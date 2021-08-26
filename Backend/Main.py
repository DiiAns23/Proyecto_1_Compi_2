from flask import Flask, request
import json
from flask.helpers import url_for
from werkzeug.utils import redirect
from Analizador_Sintactico import parse as Analizar
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from Analizador_Lexico import tokens
from Analizador_Lexico import lexer, errores
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Funcion import Funcion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Identificador import Identificador
from Instrucciones.Llamada_Funcion import Llamada_Funcion
from Instrucciones.If import If
from Analizador_Sintactico import agregarNativas as Nativas
from flask_cors import CORS

app = Flask(__name__, template_folder="Templates")
CORS(app)

@app.route('/codigo', methods=["PUT"])
def analize():
    if request.method == "PUT":
        print("Entro aqui :3")
        inpt = request.form["inpt"]
        global tmp_val
        tmp_val = inpt
        instrucciones = Analizar(tmp_val)
        ast = Arbol(instrucciones)
        TsgGlobal = Tabla_Simbolos()
        ast.setTSglobal(TsgGlobal)

        for error in errores:
            ast.getExcepciones().append(error)
            ast.updateConsola(error.toString())

        for instruccion in ast.getInst():
            if isinstance(instruccion, Funcion):
                ast.setFunciones(instruccion)
            if isinstance(instruccion, Declaracion):
                value = instruccion.interpretar(ast,TsgGlobal)
                if isinstance(value, Excepcion):
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())

        for instruccion in ast.getInst():
            if isinstance(instruccion, Imprimir):
                value = instruccion.interpretar(ast,TsgGlobal)
                if isinstance(value, Excepcion):
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())
            if isinstance(instruccion, Identificador):
                value = instruccion.interpretar(ast,TsgGlobal)
                if isinstance(value, Excepcion):
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())
            if isinstance(instruccion, Llamada_Funcion):
                value = instruccion.interpretar(ast,TsgGlobal)
                if isinstance(value, Excepcion):
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())
            #value = instruccion.interpretar(ast,TsgGlobal)
            # if isinstance(value, Excepcion):
            #         ast.getExcepciones().append(value)
            #         ast.updateConsola(value.toString())
        print(ast.getConsola())
        consola = ast.getConsola()
        return consola

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
    instrucciones = Analizar(tmp_val)
    ast = Arbol(instrucciones)
    TsgGlobal = Tabla_Simbolos()
    ast.setTSglobal(TsgGlobal)
    Nativas(ast)
    for error in errores:
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())

    for instruccion in ast.getInst():
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion)
        if isinstance(instruccion, Declaracion):
            value = instruccion.interpretar(ast,TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())

    for instruccion in ast.getInst():
        if isinstance(instruccion, Imprimir):
            value = instruccion.interpretar(ast,TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
        if isinstance(instruccion, Identificador):
            value = instruccion.interpretar(ast,TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
        if isinstance(instruccion, Llamada_Funcion):
            value = instruccion.interpretar(ast,TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
        if isinstance(instruccion, If):
            value = instruccion.interpretar(ast,TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())

    consola = ast.getConsola()
    return json.dumps(consola)

if __name__ == '__main__':
    app.run(debug = True, port=5200)