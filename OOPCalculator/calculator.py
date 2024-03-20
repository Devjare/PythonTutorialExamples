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
            Las funciones lambda son una "abreviacion" de una funcion que realiza una sola operacion.
            
            Por ejemplo, la funcion para elevar al cuadrado un numero puede ser:
            
            def elevar_cuadrado(num: int) -> int:
                return num ** 2 # Asi se eleva al cuadrado en python.
                
            Pero dicha funcion realiza una sola operacion, por tanto una lamda se puede usar en su lugar:
            
            elevar_cuadrado = lambda num: num ** 2
            
            Y realizan lo mismo, ambas definiciones pueden llamarse como una funcion normal y devuelven el mismo tipo de dato:
            
            elevar_cuadrado(num),
            
            En este ejemplo, el diccionario "operations", contiene las operaciones posibles como lalve, y como valor
            una funcion lambda con la operacion correspondiebte, sobre los valores / atributos de la clase (operandos)
        """
        self.operations = {
            "+": lambda: self.left_op + self.right_op,
            "-": lambda: self.left_op - self.right_op,
            "*": lambda: self.left_op * self.right_op,
            "/": lambda: self.left_op / self.right_op
        }

    def calculate(self):
        return self.operations[self.operator]()
