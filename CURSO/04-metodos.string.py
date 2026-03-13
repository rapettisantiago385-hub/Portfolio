animal = "  chancho feliz  "
print(animal.upper()) #el upper pone el string seleccionado en mayusculas
print(animal.lower()) #el upper pone el string en minusculas
print(animal.capitalize()) #convierte el primer caracter en mayuscula (muy util)
print(animal.title()) #convierte la primera letra de cada palabra en mayusculas
print(animal.strip()) #remueve los espacios en blanco a la derecha e izquierda del string
print(animal.strip().capitalize()) # combinar metodos de string (se separan por puntos) 
print(animal.rstrip()) #quita los espacios de la derecha
print(animal.lstrip()) # quita los espacios de la izquierda
print(animal.find("ch")) #devuelve el indice #si da -1 no encontro el indice
print(animal.replace("ch","j")) #reemplaza las letras seleccionadas por lo seleccionado
print("ch" in animal) #devuelve booleano, muestra si el caracter esta en el string
print("ch" not in animal) #devuelve en booleano, busca si el texto no esta en el string