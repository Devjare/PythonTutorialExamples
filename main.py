# En python, cada archivo es un "modulo", los directorios no son modulos a
# menos que se incluya un archivo (usualmente en blanco) llamado
# "__init__.py". Aqui importamos Task, del modulo (directorio con archivo
# __init__.py) TaskManager, que tiene el modulo (archivo .py) Task, y dentro
# de ese modulo se encuentra la clase Task que nos interesa.
import os.path

from TaskManager.Task import Task
from typing import List

if __name__ == "__main__":

    task_list: List[Task] = []

    print("Lista de tareas actual: ")
    print(str(task_list))

    opcion = input("Deseas agregar una nueva tarea? (S/N) ")
    # strip() es un metodo de cadenas para remover los espacios extras al
    # principio y final de la cadena (e.g., "   hola ", se convierte en "hola"
    while opcion.strip() != "N":
        titulo = input("Titulo: ")
        descripcion = input("Descripcion: ")
        nueva_tarea = Task(titulo=titulo, descripcion=descripcion)

        task_list.append(nueva_tarea)

        print("Lista de tareas actual: ")
        print(str(task_list))

        opcion = input("Deseas agregar una nueva tarea? S/N")

    guardar = input("Deseas guardar la lista en un archivo? (S/N) ")
    if guardar.strip() == "S":
        nombre_archivo = input("Con que nombre: ")
        if os.path.exists(os.path.join(os.getcwd(), nombre_archivo)):
            print("Guardando...")
            print("Archivo ya existe, sobre escribir? (S/N) ")
            sobreescribir = input()
            if sobreescribir.strip() == "S":
                print("Sobre escribiendo archivo...")
                with open(nombre_archivo, "a") as file:
                    for tarea in task_list:
                        file.write(str(tarea) + "\n")
            else:
                print("Agregando a archivo existente...")
                with open(nombre_archivo, "a") as file:
                    for tarea in task_list:
                        file.write(str(tarea) + "\n")

        with open(nombre_archivo, "w") as file:
            for tarea in task_list:
                file.write(str(tarea) + "\n")

    else:
        print("Terminando sin guardar...")