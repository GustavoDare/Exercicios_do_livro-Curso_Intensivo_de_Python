# Autor: Gustavo Daré
# Data: 19/09/2022

'''
Crie uma classe chamada Restaurant. O método __init__() de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. 
    Crie um método chamado describe_restaurant() que mostre essas duas informações, e um método de nome open_restaurant() que exiba uma 
    mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois atributos individualmente e, em seguida, chame os dois métodos.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()} é do tipo {self.cuisine_type.title()}.")

    def open_restuarant(self):
        print(f"O restaurante {self.restaurant_name.title()} está aberto.")

restaurant = Restaurant('afrikan house', 'buffet')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
