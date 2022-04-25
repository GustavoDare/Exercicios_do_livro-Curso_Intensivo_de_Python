# Autor: Gustavo Daré
# Data: 25/04/2022

'''
Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5 que 
    faça o seguinte, pelo menos uma vez:
        - Use um teste condicional na instrução while para encerrar o 
            laço;
        - Use uma variável active para controlar o tempo que o laço 
            executará;
        - Use uma instrução break para sair do laço quando o usuário 
            fornecer o valor 'quit'.
'''

# Versões do exercício 4 do capítulo 7

# Versão 1
print("\nVERSÃO 1")
ingrediente = ""
while ingrediente.lower() != 'quit':
    ingrediente = input("\nCaso queira finalizar digite 'quit'.\n"
        "Coloque o ingrediente que deseja colocar na pizza: ")

    if ingrediente.lower() != 'quit':
        print(f"{ingrediente.title()} foi adicionado a sua pizza!")

# Versão 2
print("\nVERSÃO 2")
active = True
while active:
    ingrediente = input("\nCaso queira finalizar digite 'quit'.\n"
        "Coloque o ingrediente que deseja colocar na pizza: ")

    if ingrediente.lower() != 'quit':
        print(f"{ingrediente.title()} foi adicionado a sua pizza!")
    else:
        active = False

# Versão 3
print("\nVERSÃO 3")
while True:
    ingrediente = input("\nCaso queira finalizar digite 'quit'.\n"
        "Coloque o ingrediente que deseja colocar na pizza: ")

    if ingrediente.lower() != 'quit':
        print(f"{ingrediente.title()} foi adicionado a sua pizza!")
    else:
        break
