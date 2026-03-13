import string
import random
import tkinter as tk 

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in  range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena 
while True:
 longitud = int(input("Cual es la longitud de la contraseña deseada?: "))
 nueva_contrasena = generar_contrasena(longitud)
 print(f"Su contraseña es: {nueva_contrasena}")