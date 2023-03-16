"""
Escreva um programa que pergunte qual é o número favorito de um usuário. Use json.dump() para armazenar esse número em um arquivo. Escreva um programa separado que leia esse valor e apresente a mensagem “Eu sei qual é o seu número favorito! É _____.”.
"""

import json

numero_favorito = int(input("Digite seu número favorito: "))
arquivo = 'Capítulo 10/numeros_favoritos.json'
with open(arquivo, 'w') as file_object:
    json.dump(numero_favorito, file_object)
