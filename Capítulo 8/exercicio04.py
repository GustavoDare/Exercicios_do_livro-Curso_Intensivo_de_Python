# Autor: Gustavo Daré
# Data: 15/05/2022

'''
Modifique a função "make_shirt()" de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie uma camiseta
    grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente.
'''

def make_shirt(tamanho = "G", estampa = "Eu amo Pyhton"):
    print(f"O tamanho da camiseta pedida é {tamanho}.")
    print(f"A estampa da camiseta vai ser '{estampa}'.\n")

# Tamanjo e estampa default
make_shirt()
# Estampa default
make_shirt("M")
# Nenhum valor default
make_shirt("P", "Eu adoro Java")
# Tamanho default
make_shirt(estampa = "Eu gosto muito de C")
