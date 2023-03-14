'''
Comece com seu programa do Exercício 9.1 (página 225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie uma instância chamada restaurant a partir dessa classe. Apresente o número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente.
Adicione um método chamado set_number_served() que permita definir o número de clientes atendidos. Chame esse método com um novo número e mostre o valor novamente.
Acrescente um método chamado increment_number_served() que permita incrementar o número de clientes servidos. Chame esse método com qualquer número que você quiser e que represente quantos clientes foram atendidos, por exemplo, em um dia de funcionamento.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()} é do tipo {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()} está aberto.")

    def set_number_served(self, number_clients):
        self.number_served = number_clients

    def increment_number_served(self, number_clients):
        self.number_served += number_clients

    def show_number_served(self):
        print(f"O número de clientes servidos no dia foi: {self.number_served}")

restaurant = Restaurant('afrikan house', 'buffet')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()

print('\n')
restaurant.show_number_served()
restaurant.number_served = 40
restaurant.show_number_served()
restaurant.set_number_served(50)
restaurant.show_number_served()
restaurant.increment_number_served(20)
restaurant.show_number_served()
