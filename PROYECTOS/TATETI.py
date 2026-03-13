tablero = [[" "for _ in range(3)]for _ in range(3)]

turno = "x"

ganador = None

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero):
    for fila in tablero:
        if fila [0] == fila [1] == fila [2] != " ":
            return fila[0]
    for col in range(3):
        if tablero[0][col] ==tablero[1][col] == tablero [2][col] != " ":
            return tablero[0][col]
    if tablero [0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero [1][1] == tablero [2][0] != " ":
        return tablero[0][2]
    return None
while True:
    mostrar_tablero(tablero)
    print(f"Turno de {turno}")

    try:
        fila = int(input("Elige fila (o-2): "))
        columna = int(input("elgie columna (0-2): "))
    except ValueError:
        print("Ingresa numeros validos")
        continue
    if tablero[fila][columna] != " ":
        print("Esta casilla esta ocupada")
        continue
    tablero[fila][columna] = turno

    ganador = verificar_ganador(tablero)
    if ganador:
        mostrar_tablero(tablero)
        print(f"¡Felcidades! {ganador} gano el juego")
        break
    if all (celda != " " for fila in tablero for celda in fila):
        mostrar_tablero(tablero)
        print("¡Empate!")
        break
    turno = "o" if turno == "x" else "x"