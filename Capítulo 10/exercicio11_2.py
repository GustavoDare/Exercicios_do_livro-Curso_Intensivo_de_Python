# Continuação do exercício 11
# 'Escreva um programa separado que leia esse valor e apresente a mensagem “Eu sei qual é o seu número favorito! É _____.”.'

import json

arquivo = 'Capítulo 10/numeros_favoritos.json'
with open(arquivo, 'r') as file_object:
    texto = json.load(file_object)
    print(f"Eu sei qual é seu número favorito. É {texto}.")
