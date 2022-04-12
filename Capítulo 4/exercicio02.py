# Autor: Gustavo Daré
# Data: 11/04/2022

# Criar uma lista com 3 animais diferentes com uma característica em comum, escrever uma mensagem para cara animal
#     (utilizando for) e escrever uma mensagem fora do laço for falando quando a característica em comum deles.

aves = ["gavião", "urubu", "pelicano"]
for ave in aves:
    print(f"O {ave.title()} é um animal carnívoro.")
print("\nTodos esses animais possuem asas.\n")
