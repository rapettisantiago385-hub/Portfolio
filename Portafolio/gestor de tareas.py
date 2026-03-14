import json
import tkinter as tk
from tkinter import messagebox


archivo = "tareas.json"

def cargar_tareas():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except:
        return []

def guardar_tareas(tareas):
    with open(archivo, "w") as f:
        json.dump(tareas, f)


def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        estado = "✔" if tarea["completada"] else "❌"
        lista_tareas.insert(tk.END, f"{tarea['texto']} [{estado}]")


def agregar_tarea_gui():
    texto = entrada_tarea.get()
    if texto.strip() != "":
        tareas.append({"texto": texto, "completada": False})
        guardar_tareas(tareas)
        actualizar_lista()
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Escriba una tarea")


def completar_tarea_gui():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        guardar_tareas(tareas)
        actualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Seleccione una tarea")


def eliminar_tarea_gui():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        guardar_tareas(tareas)
        actualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Seleccione una tarea")


ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x500")


lista_tareas = tk.Listbox(ventana, width=40, height=15)
lista_tareas.pack(pady=10)

entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea_gui)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea_gui)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea_gui)
boton_eliminar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack(pady=20)


tareas = cargar_tareas()
actualizar_lista()

ventana.mainloop()