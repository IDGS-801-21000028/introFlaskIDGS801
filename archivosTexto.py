from io import open


# Escritura de archivos
# archivo1 = open('archivo.txt', 'a')
# archivo1.write("Saludo IDGS801 Nuevo \n")
# archivo1.close()

# Lectura de archivos
archivo1 = open('archivo.txt','r')
# print(archivo1.read())
# archivo1.seek(10) #Cursor
# print(archivo1.read())

#print(archivo1.readlines())

for d in archivo1.readlines():
  print(d.rstrip())

archivo1.close()