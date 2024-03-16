import os

nombre_archivo = "archivo.txt"
archivo = None
contenido = ""
modo = "r"

if __name__ == "__main__":
    # Leer archivo
    ## Si no existe, crear
    if os.path.exists(os.path.join(os.getcwd(), nombre_archivo)):
        modo = "r"
        archivo = open(file=nombre_archivo, mode=modo)
        # join() es una funcion de cadenas, que une una cadena, con un arreglo,
        # usando como separador la cadena usada.
        # e.g. ",".join([1,2,3,4]), devuelve una cadena de los numeros separados
        # por coma: "1,2,3,4".
        contenido = "\n".join(archivo.readlines())
        archivo.close()
    else:
        # Hay diversas formas de crear archivos,
        # usando mode="w" en lugar de "r", automaticamente
        # crea el archivo si no existe.
        modo = "w"
        archivo = open(file=nombre_archivo, mode=modo)

    nuevo_contenido = ""
    while "." not in nuevo_contenido:
        # Mientras no se escriba un punto.
        nuevo_contenido += input("") + "\n"

    # Escribir en archivo
    # Si existe, agregar (append) a ese archivo
    if modo == "r":
        with open(file=nombre_archivo, mode="a") as file:
            file.write(nuevo_contenido)
    else:
        with open(file=nombre_archivo, mode="w") as file:
            file.write(nuevo_contenido)
