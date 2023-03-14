# Autor: Gustavo Daré
# Data: 17/04/2022

# Crie uma tupla com 5 comidas, exiba com um laço for, sobreescreva a tupla alterando duas comidas e exiba a nova tupla

comidas = ("feijoada", "estrogonofe", "macarronada", "lasanha", "arroz")
print("\nO cardápio é:")
for comida in comidas:
    print(comida.title())

comidas = ("creme de milho", "estrogonofe", "macarronada", "lasanha", "salada")
print("\nO cardápio modificado é:")
for comida in comidas:
    print(comida.title())
