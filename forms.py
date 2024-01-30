from wtforms import Form
from wtforms import StringField, TelField, IntegerField
from wtforms import EmailField

class UserForm(Form):
  nombre = StringField("nombre")  
  apaterno = StringField("apaterno")
  amaterno = StringField("materno")
  email = EmailField("email")
  edad = IntegerField("edad")