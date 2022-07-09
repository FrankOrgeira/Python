#!/usr/bin/env python3

from PIL import Image
from multiprocessing import Pool
import os


def conv_image(src,dest):
	im = Image.open(src)
	im = im.convert("1") # Convierte la imagen a blanco y negro
	im = im.rotate(90) # Gira la imagen 90 grados en sentido del reloj
	im = im.resize((128,128)) # Cambia el tamaño de la imágen
	im = im.save(dest)


src = os.getcwd()
dest = src + "/opt/icons/"
directorio = os.listdir(src)
print("Los archivos dentro de "+src+" son:")
for archivo in directorio:
	if os.path.isfile(archivo) and archivo.startswith(".") is False and archivo.endswith(".py") is False:
		print(archivo)
		conv_image(archivo,dest+archivo+".jpeg")
