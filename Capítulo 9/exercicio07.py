'''
Um administrador é um tipo especial de usuário. Escreva uma classe chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226), ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene uma lista de strings como "can add post", "can delete post" "can ban user", e assim por diante. Escreva um método chamado show_privileges() que liste o conjunto de privilégios de um administrador. Crie uma instância de Admin e chame seu método.
'''

from exercicio05 import User

class Admin(User):

    def __init__(self, first_name, last_name, age, profission):
        super().__init__(first_name, last_name, age, profission)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Os seus privilégios como administrador são:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin1 = Admin('Gustavo', 'Silva', 34, 'administrador')
print('\n')
admin1.describe_user()
admin1.show_privileges()
