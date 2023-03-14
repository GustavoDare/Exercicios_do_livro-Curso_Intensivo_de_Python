# Autor: Gustavo Daré
# Data: 25/04/2022

'''
Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito, 
    exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário, informe que sua mesa está pronta.
'''

reserva = int(input("Você gostaria de uma mesa para quantas pessoas? "))

if reserva > 8:
    print("Para essa quantidade, peço que vocês esperem vagar espaço.")
else:
    print("Temos uma mesa disponível. Me acompanhem, por favor.")
