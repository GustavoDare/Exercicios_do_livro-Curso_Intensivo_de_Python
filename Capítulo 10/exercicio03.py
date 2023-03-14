"""
Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
"""

nome_usuario = input("Digite seu nome de usuário: ")

with open('Capítulo 10\guest.txt', 'w', encoding="utf8") as file_object:
    file_object.write(nome_usuario)
