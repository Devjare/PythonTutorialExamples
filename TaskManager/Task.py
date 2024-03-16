class Task:

    def __init__(self, titulo: str, descripcion: str) -> None:
        self.titulo = titulo
        self.descripcion = descripcion

    # Por convencion, las funciones / metodos que esten rodeados por dos
    # guiones bajos, son funciones de python, estas funciones tambien son
    # comunmente llamadas "Dunder methods".
    # __init__, sirve para iniciarlizar los datos de la clase, con lo que se
    # pase por parametro. En otros lenguajes esto seria el equivalente al
    # "Constructor" de la clase.
    # __str__ sobre escribe la funcion str() sobre esta clase, sirve para
    # utilizar str(objeto) sobre datos no primitivos (como la clase Task que
    # esta definida por nosotros) y devuelva la representacion en forma de
    # string que deseas tenga el objeto de tu clase.
    def __str__(self):
        return f"Tarea:\n\tTitulo: {self.titulo},\n\tDescripcion: {self.descripcion}"

    # __repr__ es similar a str, pero usulamente es usado para proporcionar
    # informacion mas tecnica del objeto.
    # Estos "Dunder methods" son utlies en algunas situaciones.
    # Por ejemplo, si tienes una lista/arreglo de tareas(Task) y quieres
    # compararlos. Para un tipo de dato primitivo (int, float, bool, str),
    # por lo genearl es posible hacer algo como lista1 == lista2, y funciona.
    # Para lsitas de objetos de clases definidas por usuario, es posible si
    # utilizas los dunder methods. __eq__, y __repr__, son dos ejemplos de
    # estos.
    # En el ejemplo en "main.py", se imprime la lista completa de tareas,
    # y muestra informacion legible, estoy es posible gracias a la
    # implementacion de __repr__.
    def __repr__(self):
        return f"Task(titulo={self.titulo}, descripcion={self.descripcion})"
