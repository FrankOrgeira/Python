#!/usr/bin/env python3

import os
import requests

# Este script permite leer todos los archivos.txt de comentarios de un directorio
# convertirlos en un diccionario y subirlos a un web server mediante POST

# Creo el diccionario
comentarios = {} 

# Asigno a la variable dest el nombre del directorio a leer 
dest = "/data/feedback/"

# Asigno a el arreglo directorio el contenido del directorio 
directorio = os.listdir(dest)

print ("Los archivos de comentario son: ")

# Asigno a la variable Id el valor 1 para index el arreglo
Id = 1

# Hago un for para ir leyendo uno por uno los archivos de texto del directorio
for archivo in directorio:

	# Si el nombre de archivo contiene .txt al final proceso
	if archivo.endswith(".txt") is True:
		print(archivo)

		# Abro el archivo del directorio, nombre con with para que al terminar lo cierre automáticamente
		with open (dest+archivo) as file:

			# Si ese número de id no está presente en el directorio lo proceso
			if id not in comentarios:

				# Leo las lineas del archivo de texto, asignando a cada variable para almacenar en el directorio
				title = file.readline()
				name = file.readline()
				date = file.readline()
				feedback = file.readline()

				# Asigno el formato de almacenamiento de los datos en el directorio y almaceno
				comentarios = {"id": id, "title": title, "name": name, "date":date, "feedback": feedback}

				# Asigno a la variable form_data el contenido del diccionario
				form_data = comentarios

				# Asigno a la variable respuesta el valor que devuelve el web server al ejecutar la petición POST  
				respuesta = requests.post('http://35.232.50.168/feedback/', data=form_data)
				
				# Valido la respuesta del web server, si devuelve 201 todo salió OK, en caso contrario, hubo un error
				if respuesta = 201:
					print("El archivo "+archivo+" se subió correctamente al web server")
				else
					print("Hubo un problema de comunicación")