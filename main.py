from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#   return "Hola mundo"

@app.route("/hola")
def hola():
  return "<h1>Saludos desde hola prueba refresh</h1>"

@app.route("/Saludo")
def saludo():
  return "<h1>Saludos desde saludo</h1>"

# Rutas para recibir datos mediante la URL (GET)
@app.route("/nombre/<string:nom>")
def nombre(nom):
  return "<h1>Saludos "+nom+"</h1>"

@app.route("/numero/<int:n1>")
def numero(n1):
  return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nombre>")
def func(id, nombre):
  return "<h1>ID: {} Nombre: {}</h1>".format(id,nombre)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
  return "<h1>La suma {} + {} = {}</h1>".format(n1,n2,n1+n2)

# Se pueden usar dos decoradores para un valor default (Si no se recibe un valor muestra el default)
@app.route("/default")
@app.route("/default/<string:d>")
def func2(d = "Dario"):
  return "<h1>El nombre de User es: {}</h1>".format(d)

# Obtener una pagina desde otra carpeta (Templates)
@app.route("/")
def index():
  return render_template("index.html")

# Enviar datos del back al front
@app.route("/alumnos")
def alumnos():
  titulo = "UTL !!!"
  nombres = ["Mario","Pedro","Juan","Dario"]
  return render_template("alumnos.html",titulo=titulo, nombres=nombres)

@app.route("/maestros")
def maestros():
  return render_template("maestros.html")






if __name__ == "__main__":
  app.run(debug=True)