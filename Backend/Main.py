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

    for instruccion in ast.getInst():
        if not (isinstance(instruccion, Funcion)):
            value = instruccion.interpretar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Return fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Break fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Continue fuera de ciclo", instruccion.fila, instruccion.colum)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
    consola = ast.getConsola()
    return json.dumps(consola)

if __name__ == '__main__':
    app.run(debug = False, port=5200)