# Autor: Gustavo Daré
# Data: 11/04/2022

# Crie uma lista dos múltiplos de 3, de 3 a 30 e exiba-a utilizando o 
#     laço for

# Jeito 1
print(f"\nJeito 1")
multiplos_de_3 = list(range(3, 31, 3))
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)

# Jeito 2
print(f"\nJeito 2")
multiplos_de_3 = []
for valor in range(1, 11):
    multiplos_de_3.append(valor*3)
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)

# Jeito 3
print(f"\nJeito 3")
multiplos_de_3 = [valor*3 for valor in range(1, 11)]
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)
