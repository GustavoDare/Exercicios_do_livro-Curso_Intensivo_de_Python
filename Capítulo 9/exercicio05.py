'''
Acrescente um atributo chamado login_attempts à sua classe User do Exercício 9.3 (página 226). Escreva um método chamado increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts() várias vezes. Exiba o valor de login_attempts para garantir que ele foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para garantir que seu valor foi reiniciado com 0.
'''

class User():

    def __init__(self, first_name, last_name, age, profission):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = age
        self.profission = profission
        self.login_attempts = 0

    def describe_user(self):
        print(f'O(A) {self.full_name} tem {self.age} anos e sua profissão é: {self.profission}.')
    
    def greet_user(self):
        print(f"Seja muito bem vindo(a), {self.full_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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

print('\n')
for x in range(0, 5):
    user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
