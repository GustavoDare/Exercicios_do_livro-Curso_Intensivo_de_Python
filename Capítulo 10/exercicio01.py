"""
Abra um arquivo em branco em seu editor de texto e escreva algumas linhas que sintetizem o que você aprendeu sobre Python até agora. Comece cada linha com a expressão Em Python podemos.... Salve o arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios deste capítulo. Escreva um programa que leia o arquivo e mostre o que você escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with.
"""

# Lendo o arquivo todo
with open('Capítulo 10\learning_python.txt', 'r', encoding="utf8") as file_object:
    texto = file_object.read()
    print("Modo 1:")
    print(texto)

# Percorrendo o objeto arquivo com um laço
with open('Capítulo 10\learning_python.txt', 'r', encoding="utf8") as file_object:
    print("Modo 2:")
    for linha in file_object:
        print(linha.rstrip())

# Armazenando as linhas em uma lista e trabalhando com ela fora do bloco with
with open('Capítulo 10\learning_python.txt', 'r', encoding="utf8") as file_object:
    linhas_texto = file_object.readlines()
print("\nModo 3:")
for linha_texto in linhas_texto:
    print(linha_texto.rstrip())
