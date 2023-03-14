'''
Escreva uma classe Privileges separada. A classe deve ter um atributo privileges que armazene uma lista de strings conforme descrita no Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma instância de Privileges como um atributo da classe Admin. Crie uma nova instância de Admin e use seu método para exibir os privilégios.
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

class Admin(User):

    def __init__(self, first_name, last_name, age, profission):
        super().__init__(first_name, last_name, age, profission)
        self.privileges = Privileges()

class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can add user"]

    def show_privileges(self):
        print("Os seus privilégios como administrador são:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin1 = Admin('Thiago', 'Costa', 40, 'administrador')
admin1.describe_user()
admin1.privileges.show_privileges()
