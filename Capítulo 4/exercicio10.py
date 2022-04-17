# Autor: Gustavo Daré
# Data: 17/04/2022

# Usando um exercício desse capítulo, exibir os 3 elementos do inicío, do meio 
#     e do final da lista, utilizando fatias

# Exercício 06
impares = list(range(1, 20, 2))
for impar in impares:
    print(impar)

print(f"Os 3 primeiros elementos da lista são: {impares[:3]}")
print(f"Os 3 elementos do meio da lista são: {impares[4:7]}")
print(f"Os 3 últimos elementos da lista são: {impares[-3:]}")
