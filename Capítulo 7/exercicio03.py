# Autor: Gustavo Daré
# Data: 25/04/2022

'''
Peça um número ao usuário e, em seguida, informe se o número é múltiplo
    de dez ou não.
'''

numero = int(input("Digite um número e direi se ele é múltiplo de 10: "))

if numero % 10 == 0:
    print(f"O número {numero} é múltiplo de 10.")
else:
    print(f"O número {numero} não é múltiplo de 10.")
