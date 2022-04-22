# Autor: Gustavo Daré
# Data: 22/04/2022

# Crie um dicionário com 3 rios importantes e seus respectivos países,
#     exiba uma mensagem para cada par chave-valor, exiba apenas as 
#     chaves (rios), e exiba apenas os valores (países)

glossário = {'nilo': 'egito', 'ganges': 'índia', 'volga': 'rússia'}

for rio, país in glossário.items():
    print(f"O rio {rio.title()} corre pelo(a) {país.title()}.")

print("\nAlguns dos rios mais famosos são:")
for rio in glossário.keys():
    print(rio.title())

print("\nOs países que contém esses rios são:")
for país in glossário.values():
    print(país.title())
