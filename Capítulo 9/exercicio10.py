"""
Usando sua classe Restaurant mais recente, armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
Crie uma instância de Restaurant e chame um de seus métodos para mostrar que a instrução import funciona de forma apropriada
"""

from exercicio10_modulo import Restaurant

restaurant = Restaurant('burguer king','fast food')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(80)
restaurant.show_number_served()
restaurant.increment_number_served(20)
restaurant.show_number_served()
