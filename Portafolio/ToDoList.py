import json 
archivo = "tareas.json"

def cargar_tareas():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except:
        return[]
    

def guardar_tareas (tareas):
    with open(archivo, "w") as f:
        json.dump (tareas, f)
    
def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas): 
            estado = "Hecho" if tarea ["completada"] else "No hecho"
            print(f" {i+1}. {tarea['texto']}[{estado}]")

def agregar_tarea(tareas): 
    texto = input("Escriba una tarea: ")
    tareas.append({
        "texto":texto,
        "completada": False
    })
def completar_tarea(tareas):
    ver_tareas(tareas)
    num = int(input("Numero de tarea completada: ")) - 1
    if 0 <= num < len(tareas):
        tareas[num]["completada"] = True

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    num = int(input("Numero de tarea a eliminar: ")) - 1
    if 0 <= num < len(tareas):
        tareas.pop(num)

tareas = cargar_tareas()

while True:
    print("\nGESTOR DE TAREAS")
    print("1 - Ver tareas")
    print("2 - Agregar tarea")
    print("3 - Completar tarea")
    print("4 - Eliminar tarea")
    print("5 - Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1": 
            ver_tareas(tareas)
        case "2":
            agregar_tarea(tareas)
            guardar_tareas(tareas)
        case "3":
            completar_tarea(tareas)
            guardar_tareas(tareas)
        case "4": 
            eliminar_tarea(tareas)
            guardar_tareas(tareas)
        case "5":
            guardar_tareas(tareas)
            break
        case _:
            print("Opcion no valida")