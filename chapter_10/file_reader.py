from pathlib import Path

path = Path("scratch.txt") # la librería que ayuda a trabajar con las rutas de archivos
contents = path.read_text() # lee el texto del documento
contents = contents.rstrip() # remueve la linea final del documento

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip() #lstrip es left strip quitar espacios izquierda

print(pi_string)
print(len(pi_string))