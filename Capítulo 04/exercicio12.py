# Autor: Gustavo Daré
# Data: 17/04/2022

# Copiar o arquivo foods.py do capítulo 4 do livro e imprimir as listas com um laço for

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())
