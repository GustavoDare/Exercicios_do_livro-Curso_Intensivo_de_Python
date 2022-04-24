# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Crie vários dicionários, em que o nome de cada dicionário seja o nome 
    de um animal de estimação. Em cada dicionário, inclua o tipo do
    animal e o nome do dono. Armazene esses dicionários em uma lista 
    chamada pets. Em seguida, percorra sua lista com uma laço e, à 
    medida que fizer isso, apresente tudo que você sabe sobre cada 
    animal de estimação.
'''

thor = {'nome': 'thor', 'tipo': 'cachorro', 'dono': 'lucas'}
raio = {'nome': 'raio', 'tipo': 'gato', 'dono': 'olívia'}
flor = {'nome': 'flor', 'tipo': 'canário', 'dono': 'pâmela'}
mel = {'nome': 'mel', 'tipo': 'hamster', 'dono': 'lucas'}
pets = [thor, raio, flor, mel]

for pet in pets:
    print(f"O(A) {pet['dono'].title()} possui um {pet['tipo']} de animal de "
        f"estimação que se chama {pet['nome'].title()}.")