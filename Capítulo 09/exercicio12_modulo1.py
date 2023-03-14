# Classe User que será importada e testada no exercício 12

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
