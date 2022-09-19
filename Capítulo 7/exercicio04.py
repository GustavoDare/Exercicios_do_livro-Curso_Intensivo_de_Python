# Autor: Gustavo Daré
# Data: 25/04/2022

'''
Escreva um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja fornecido. 
    À medida que cada ingrediente é especificado, apresente uma mensagem informando que você acrescentará esse ingrediente à pizza.
'''

ingrediente = ""
while ingrediente.lower() != 'quit':
    ingrediente = input("\nCaso queira finalizar digite 'quit'.\n"
        "Coloque o ingrediente que deseja colocar na pizza: ")

    if ingrediente.lower() != 'quit':
        print(f"{ingrediente.title()} foi adicionado a sua pizza!")
