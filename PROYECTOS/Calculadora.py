print("\nBienvenido a la calculadora de Python!")
opciones = int(input("Ingresa una de las siguientes opciones: \n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n"))

num1 = int(input("Ingresa el primer numero: ")) 
num2 = int(input("Ingrese el segundo numero: "))

match opciones:
    case 1:
        suma = num1 + num2
        print(f"El resultado de la suma es: {suma}")
    case 2:
        resta = num1 - num2
        print(f"El resultado de la resta es: {resta}")
    case 3:
        multiplicacion = num1 * num2
        print(f"El resultado de  la multipliación es: {multiplicacion} ")
    case 4: 
        division = num1 / num2
        print(f"El resultado de la división es: {division}")
    case _:
        print("Operacion no valida X")