import random  # importamos libreria random casos 'aleatorios'
import os  # importamos libreria para interactuar con archivos
from constantes import bienvenida, despedida


print(bienvenida)

# Usamos la libreria os para obtener la lista de archivos dentro de la carpeta fotos
lista_de_fotos = os.listdir("fotos")

# Imprimimos los archivos de fotos disponibles
print("Opciones disponibles:")
for e in lista_de_fotos:
  print("- " + str(e))

input("Presiona ENTER para obtener una foto al azar de perritos ")

# Usamos la funcion choice de random para obtener una foto al azar
foto_aleatoria = random.choice(lista_de_fotos)

# Concatenamos para obtener la ruta completa de la foto
ruta_foto = os.path.join("fotos",foto_aleatoria)

# Usamos la liberia os para abrir la foto seleccionada
os.startfile(ruta_foto)

print(despedida)
