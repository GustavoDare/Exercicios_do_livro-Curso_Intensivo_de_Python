'''
Uma sorveteria é um tipo específico de restaurante. Escreva uma classe chamada IceCreamStand que herde da classe Restaurant escrita no Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da classe funcionará; basta escolher aquela de que você mais gosta. Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de IceCreamStand e chame esse método.
'''

from exercicio04 import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        if self.flavors:
            if len(self.flavors) > 1:
                print("Os meus sabores de sorvetes favoritos são:")
                for flavor in self.flavors:
                    print(f'- {flavor};')
            else:
                print(f"O meu sabor de sorvete favorito é: {self.flavors[0]}")
        else:
            print("Não tenho sabor preferido de sorvete.")

sorveteria1 = IceCreamStand('borelli', 'ice cream', ['morango', 'pistache', 'mussecake de framboesa'])
sorveteria2 = IceCreamStand('vanessa', 'Ice cream', [])
sorveteria3 = IceCreamStand('chiquinho', 'ice cream', ['ovomaltine'])

print('\n')
sorveteria1.describe_restaurant()
sorveteria1.show_flavors()
sorveteria2.describe_restaurant()
sorveteria2.show_flavors()
sorveteria3.describe_restaurant()
sorveteria3.show_flavors()
