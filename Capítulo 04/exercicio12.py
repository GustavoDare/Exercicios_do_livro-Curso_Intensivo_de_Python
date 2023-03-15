"""
Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.
"""

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
