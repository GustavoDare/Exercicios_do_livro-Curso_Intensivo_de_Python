import unittest
from exercicio03 import Employee

class TesteEmployee(unittest.TestCase):
    def setUp(self):
        self.empregado = Employee("Ricardo", "Silva", 50000)

    def test_give_default_raise(self):
        self.empregado.give_raise()
        self.assertEqual(self.empregado.salario_anual, 55000)

    def test_give_custom_raise(self):
        self.empregado.give_raise(7000)
        self.assertEqual(self.empregado.salario_anual, 57000)

unittest.main()
