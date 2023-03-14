'''
Um administrador é um tipo especial de usuário. Escreva uma classe chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226), ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene uma lista de strings como "can add post", "can delete post" "can ban user", e assim por diante. Escreva um método chamado show_privileges() que liste o conjunto de privilégios de um administrador. Crie uma instância de Admin e chame seu método.
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
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Os seus privilégios como administrador são:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin1 = Admin('Gustavo', 'Silva', 34, 'administrador')
admin1.describe_user()
admin1.show_privileges()
