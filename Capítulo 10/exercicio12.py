"""
Combine os dois programas do Exercício 10.11 em um único arquivo. Se o número já estiver armazenado, informe o número favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu número favorito e armazene-o em um arquivo. Execute o programa duas vezes para garantir que ele funciona.
"""

import json

arquivo = 'Capítulo 10/numeros_favoritos.json'

try:
    with open(arquivo, 'r') as file_object:
        texto = json.load(file_object)
        print(f"Eu sei qual é seu número favorito. É {texto}.")
except FileNotFoundError:
    numero_favorito = int(input("Digite seu número favorito: "))
    with open(arquivo, 'w') as file_object:
        json.dump(numero_favorito, file_object)
