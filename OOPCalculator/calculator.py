class Calculator(object):
    OPERATORS = {
        "SUM": "+",
        "SUB": "-",
        "MUL": "*",
        "DIV": "/",
    }

    def __init__(self, left_op, right_op, operator):
        self.left_op = left_op
        self.right_op = right_op
        self.operator = operator

        """
            En python y muchos otros lenguages populares, esta implementado el paradigma de programacion
            funcional. Lenguajes orientados a este paradigma, tal y como indica su nombre, estan basados
            en el uso de funciones. Ejemplos de estos lenguajes son: haskell, lisp, y clojure.
            
            Estos lenguajes utilizan el concepto de "lazy_evaluation" para gran parte de sus funciones, esto
            fue una de las razones para incluir este paradigma en lenguajes no funcionales como python, java, 
            c++, etc. Esto esta implementado de diversas formas pero la mas directa son las funciones lambda (
            en algunos lenguajes tienen distinto nombre, como en JavaScript son arrowfunctions).
            
            Este nuevo concepto permitio la reduccion de redundancia y aumento la legibilidad en codigo al reducir
            el espacio y repeticion del uso de funciones que realizan tareas simples y comunmente se repetian mucho.
            Y una de las ventajas de esto, tanto en python como en otros lenguajes es la introduccion de un tipo
            de dato para representar funciones. En python y creo en java existe el tipo de dato llamado "Callable"
            que representa una funcion.
            
            Por ejemplo:
            
            foo: Callable
            
            dice que la variable foo es de tipo Callable, esto hace posible asignar una funcion a dicha variable:
            
            def suma(x: int, y: int) -> int:
                return x + y
                
            foo = suma
            
            sirviendo algo asi como un alias de la funcion en este caso, por tanto la funcion suma ahora puede
            ser llamada como foo():
            
            resultado = suma(x, y),
            
            es lo mismo que:
            
            resultado = foo(x, y)
            
            Ahora, con el uso de lambdas, esto tiene "mas sentido", al realizar definiciones de funciones "inline":
            
            suma = lambda x, y: x + y
            
            hace que "suma" sea una funcion que suma los dos valores que se le pasan por parametro, tal y como la 
            definicion de arriba:
            
            resultado = suma(x, y)
            
            Tarea adicional: reemplaza las funciones de esta clase, por funciones lambda*.    
        """
        self.operations = {
            "+": self.add,
            "-": self.substract,
            "*": self.multiplication,
            "/": self.division
        }

    def add(self):
        return self.left_op + self.right_op

    def substract(self):
        return self.left_op - self.right_op

    def multiplication(self):
        return self.left_op * self.right_op

    def division(self):
        return self.left_op / self.right_op

    def calculate(self):
        return self.operations[self.operator]()
