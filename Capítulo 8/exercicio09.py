# Autor: Gustavo Daré
# Data: 12/07/2022

'''
Crie uma lista de nomes de mágicos. Passe a lista para uma função 
    chamada show_magicians() que exiba o nome de cada mágico da lista.
'''

def show_magicians(magicos):
    for magico in magicos:
        print(magico.title())

magicos = ['howard thurston', 'david copperfield', 'lance burton', 
            'harry houdini', 'dynamo']
show_magicians(magicos)
