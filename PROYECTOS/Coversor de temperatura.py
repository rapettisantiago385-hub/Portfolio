temperatura = float(input("Ingrese la temperatura en Celsius: "))
while True: 
 opciones = int(input("Seleccione la unidad a convertir: \n1.Fahrenheit\n2.Kelvin\n3.Salir\n"))

 match opciones:
    case 1:
        Fahrenheit = temperatura * 1.8 + 32
        print(f"Su temperatura en Fahrenheit es: {Fahrenheit}")
    case 2:
        Kelvin = temperatura + 273.15
        print(f"Su temperatura en Kelvin es: {Kelvin}")
    case 3:
        print("Gracias por usar el conversor!")
        break
    case _:
       print(" Opcion no valida X")