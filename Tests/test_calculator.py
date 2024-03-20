import unittest

from OOPCalculator.calculator import Calculator

"""
    Las pruebas unitarias, son de gran ayuda para probar las funciones, y clases de python.
    Hoy en dia son parte del estandar para los procesos de integracion y despliegue continuos (CI/CD),
    al permitir automatizar las pruebas.
    
    Python incluye como parte de sus modulos internos el modulo "unittest" para implementar estas pruebas
    unitarias.
"""
class TestCalculator(unittest.TestCase):
    """
    Cada prueba unitaria, debe ser una funcion que empiece con la cadena "test_",
    tambien se pueden hacer clases que hereden de la clase TestCase, para agrupar dichas pruebas.
    """
    def test_sum(self):
        x = 10
        y = 20

        calculator = Calculator(x, y, Calculator.OPERATORS['SUM'])

        """
        assertEquals es el punto de la prueba, verifica que la llamada a la funcion (primer parametro)
         de el mismo resultado que el esperado (parametro dos)
        """
        self.assertEqual(calculator.calculate(), x + y)
