# Autor: Gustavo Daré
# Data: 15/05/2022

'''
Escreva uma função chamada "make_shirt()" que aceite um tamanho e o 
    texto de uma mensagem que deverá ser estampada na camiseta. A 
    função deve exibir uma frase que mostre o tamanho da camiseta e a 
    mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma 
    camiseta. Chame a função uma segunda vez usando argumentos nomeados.
'''

def make_shirt(tamanho, estampa):
    print(f"O tamanho da camiseta pedida é {tamanho}.")
    print(f"A estampa da camiseta vai ser '{estampa}'.\n")

# Argumentos posicionais
make_shirt("G", "Pyhton é a melhor linguagem de programação")

# Argumentos nomeados
make_shirt(estampa = "C é uma linguagem de programação muito boa", 
            tamanho = "M")
