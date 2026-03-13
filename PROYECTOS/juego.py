import random

print("¡bienvenido a piedra, papel o tijeras con python!")

opciones = ["piedra", "papel", "tijeras"]

usuario = input("elegi entre piedra, papel o tijeras: ").lower()

computadora = random.choice(opciones)

print(f"La computadora eligio: {computadora}")

if usuario == computadora:
    print("EMPATE")
elif usuario ==  "piedra" and computadora == "tijeras":
    print("GANASTE")
elif usuario == "papel" and computadora == "piedra":
    print("GANASTE")
elif usuario == "tijeras" and computadora == "papel":
 print("Ganaste :)")

elif usuario in opciones:
   print("Perdiste :(")
else:
   print("opcion no valida")
