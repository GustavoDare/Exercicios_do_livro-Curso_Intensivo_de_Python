# Autor: Gustavo Daré
# Data: 12/07/2022

'''
Comece com uma cópia de seu programa do Exercício 8.9. Escreva uma 
    função chamada make_great() que modifique a lista de mágicos 
    acrescentando a expressão o Grande ao nome de cada mágico. Chame 
    show_magicians() para ver se a lista foi realmente modificada.
'''

def show_magicians(magicos):
    for magico in magicos:
        print(magico.title())

def make_great(magicos):
    for x in range(len(magicos)):
        magicos[x] = 'o Grande, ' + magicos[x]

magicos = ['howard thurston', 'david copperfield', 'lance burton', 
            'harry houdini', 'dynamo']

make_great(magicos)
show_magicians(magicos)
