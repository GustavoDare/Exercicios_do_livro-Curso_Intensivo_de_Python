# Autor: Gustavo Daré
# Data: 11/04/2022

# Crie uma lista dos cubos dos números de 1 a 10 e exiba-a utilizando o
#     laço for

# Jeito 1
print("\nJeito 1")
cubos = []
for valor in range(1, 11):
    cubos.append(valor**3)
for cubo in cubos:
    print(cubo)

# Jeito 2
print("\nJeito 2")
cubos = [valor**3 for valor in range(1, 11)]
for cubo in cubos:
    print(cubo)
