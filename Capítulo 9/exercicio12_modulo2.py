# Classes Admin e Privileges que serão importadas e testadas no exercício 12

from exercicio12_modulo1 import User

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
