# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Comece com o programa que você escreveu no Exercício 6.1 (página 147).
    Crie dois novos dicionários que representem pessoas diferentes e 
    armazene os três dicionários em uma lista chamada people. Percorra 
    sua lista de pessoas com um laço. À medida que percorrer a lista, 
    apresente tudo que você sabe sobre cada pessoa.
'''

usuario1 = {"nome": "gustavo", "sobrenome": "daré", "idade": 21,
    "cidade": "são paulo"}
usuario2 = {"nome": "ana", "sobrenome": "souza", "idade": 11,
    "cidade": "florianópolis"}
usuario3 = {"nome": "otávio", "sobrenome": "silva", "idade": 40,
    "cidade": "salvador"}
people = [usuario1, usuario2, usuario3]

for pessoa in people:
    print("\nAs informações do usuário são:")
    print(f"Nome: {pessoa['nome'].title()}")
    print(f"Sobrenome: {pessoa['sobrenome'].title()}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade: {pessoa['cidade'].title()}")
