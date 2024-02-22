from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
  nombre = StringField("nombre",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])  
  apaterno = StringField("apaterno",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  amaterno = StringField("materno",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  email = EmailField("email",[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  edad = IntegerField("edad",[
    validators.DataRequired(message="El campo es requerido."),   
  ])