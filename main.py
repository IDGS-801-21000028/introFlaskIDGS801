from flask import Flask, render_template, request
from forms import UserForm
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g

app = Flask(__name__)
app.secret_key="21000028"

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

@app.route("/maestros")
def maestros():
  return render_template("maestros.html")

@app.route("/calcular", methods=["GET","POST"])
def calcular():
  if request.method == "POST":
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    return "La multiplicación de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
  else:
    return '''
      <form action="/calcular" method="POST">
        <label for="num1">N1:</label>
        <input type="text" name="n1" id="num1"><br>
        <label for="num2">N2:</label>
        <input type="text" name="n2" id="num2"><br>
        <input type="submit">
      </form>
    '''

@app.route("/OperaBas")
def operas():
  return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
  if request.method == "POST":
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    return "La multiplicación de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))

#21 de febrero de 2024
#Agregando un manejador de error
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

#Funciones before y after
@app.before_request
def before_request():
  g.nombre = "Mario"
  print("Before 1")
 
@app.after_request
def after_reques(response):
  print("After 3")
  return response

# Enviar datos del back al front
@app.route("/alumnos", methods = ['GET','POST'])
def alumnos():  
  alumno_clase = UserForm(request.form)  
  nom = ""
  apa = ""
  ama = ""
  edad = 0
  email = ""
  if request.method == 'POST' and alumno_clase.validate():
    nom = alumno_clase.nombre.data
    apa = alumno_clase.apaterno.data
    ama = alumno_clase.amaterno.data    
    email = alumno_clase.email.data
    edad = alumno_clase.edad.data 
    
    mensaje = "Bienvenido {} {}".format(nom, apa)
    flash(mensaje)
  
  print("Alumno: {}".format(g.nombre))
  return render_template("alumnos2.html", form = alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)


if __name__ == "__main__":
  app.run(debug=True)