import random

print(" ¡ADIVINA EL NUMERO QUE ELIGIO PYTHON!")

secreto = random.randint(1,20)

intentos = 0

while True: 
    intento = int(input("Adivina el numero que Pytohn eligio (1,20): "))
    intentos += 1 
    
    if intento < secreto:
        print(" Mas alto!")
    elif intento > secreto:
        print("Mas bajo!")
    else:
        print("GANASTE!!!!")
        print("adivinasDte en",intentos, "intentos")
        break #el break es para que cuando se termine el bucle(while) no se ejecute otra vez.

