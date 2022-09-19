# Autor: Gustavo Daré
# Data: 12/07/2022

'''
Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em uma lista separada. Chame show_magicians() com cada lista 
    para mostrar que você tem uma lista de nomes originais e uma lista com a expressão o Grande adicionada ao nome de cada mágico.
'''

def show_magicians(magicos):
    for magico in magicos:
        print(magico.title())

def make_great(magicos):
    for x in range(len(magicos)):
        magicos[x] = 'o Grande, ' + magicos[x]
    return magicos

magicos = ['howard thurston', 'david copperfield', 'lance burton', 'harry houdini', 'dynamo']

grandes_magicos = make_great(magicos[:])
print("Lista originial: ")
show_magicians(magicos)
print("\nCópia da lista original com 'O Grande' antes do nome: ")
show_magicians(grandes_magicos)
