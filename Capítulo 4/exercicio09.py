# Autor: Gustavo Daré
# Data: 11/04/2022

# Usar list comprehension para gera os cubos de 1 a 10

cubos = [valor**3 for valor in range(1, 11)]
for cubo in cubos:
    print(cubo)
