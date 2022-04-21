# Autor: Gustavo Daré
# Data: 21/04/2022

# Crie uma lista com os núemros de 1 a 9, percorra a lista com um laço
#     utilizando uma cadeia if-elif-else para exibir: "1st 2nd 3rd 4th 
#     5th 6th 7th 8th 9th" com cada número em uma linha.

numeros = list(range(1, 10, 1))
for numero in numeros:
    if numero == 1:
        print("1st")
    elif numero == 2:
        print("2nd")
    elif numero == 3:
        print("3rd")
    else:
        print(f"{numero}th")
