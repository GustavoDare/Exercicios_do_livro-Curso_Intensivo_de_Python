import unittest
import city_functions

class TesteCityFunctions(unittest.TestCase):

    # Teste exigido no exercício 01
    def test_city_country(self):
        localidade = city_functions.localidade('santiago', 'chile')
        self.assertEqual(localidade, 'Santiago, Chile')

    # Testes exigidos no exercício 02
    def test_city_country_modificada(self):
        localidade = city_functions.localidade_modificada('santiago', 'chile')
        self.assertEqual(localidade, 'Santiago, Chile')

    def test_city_country_population_modificada(self):
        localidade = city_functions.localidade_modificada('santiago', 'chile', populacao=5000000)
        self.assertEqual(localidade, 'Santiago, Chile - população 5000000')
 
unittest.main()
