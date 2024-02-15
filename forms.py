from wtforms import Form
from wtforms import StringField, TelField, IntegerField
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
    validators.DataRequired(message="El campo es requerido."),
    validators.email(message="Ingresa un email valido.")
  ])
  edad = IntegerField("edad",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=1, max=2, message="Error en la longitud.")
  ])