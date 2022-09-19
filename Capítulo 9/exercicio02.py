# Autor: Gustavo Daré
# Data: 19/09/2022

'''
Comece com a classe do Exercício 9.1. Crie três instâncias diferentes da classe e chame describe_restaurant() para cada instância.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()} é do tipo {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()} está aberto.")

restaurant1 = Restaurant('ruella', 'bistrô')
restaurant2 = Restaurant('tatini', 'clássico')
restaurant3 = Restaurant('amici', 'comfort food')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
