# Classe Restaurant que será importada e testada no exercício 10

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