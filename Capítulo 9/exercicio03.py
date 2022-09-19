# Autor: Gustavo Daré
# Data: 19/09/2022

'''
Crie uma classe chamada User. Crie dois atributos de nomes  first_name e last_name e, então, crie vários outros atributos normalmente 
    armazenados em um perfil de usuário. Escreva um método de nome describe_user() que apresente um resumo das informações do usuário. 
    Escreva outro método chamado greet_user() que mostre uma saudação personalizada ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois métodos para cada usuário.
'''

class User():

    def __init__(self, first_name, last_name, age, profission):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = age
        self.profission = profission

    def describe_user(self):
        print(f'O(A) {self.full_name} tem {self.age} anos e sua profissão é: {self.profission}.')
    
    def greet_user(self):
        print(f"Seja muito bem vindo(a), {self.full_name}.")

user1 = User('gustavo', 'daré', 21, 'engenheiro')
user2 = User('maria', 'silva', 30, 'advogada')
user3 = User('josé', 'alcantara neto', 28, 'estilista')
user4 = User('ana', 'machado neves', 80, 'professora')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
