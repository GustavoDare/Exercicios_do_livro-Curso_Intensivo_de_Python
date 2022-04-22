# Autor: Gustavo Daré
# Data: 22/04/2022

# Crie um dicionário com as informações: primeiro nome, sobrenome, 
#     idade e cidade; e exiba cada uma das informações

usuario = {"nome": "gustavo", "sobrenome": "daré", "idade": 21,
    "cidade": "são paulo"}

print("As informações do usuário são:")
print(f"Nome: {usuario['nome'].title()}")
print(f"Sobrenome: {usuario['sobrenome'].title()}")
print(f"Idade: {usuario['idade']}")
print(f"Cidade: {usuario['cidade'].title()}")
