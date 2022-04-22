# Autor: Gustavo Daré
# Data: 22/04/2022

# Crie um dicionário com 5 palavras de programação como chave e seus
#     significados como seus respectivos valores. Exiba a palavra 
#     seguida de dois pontos e o seu significado, colocar uma linha em 
#     branco (\n) entre as definições.

glossário = {'variável': 'Espaço na memória do computador destinado a um dado',
    'lista': 'Sequência de elemetos mutáveis durante a execução do programa',
    'tupla': 'Sequência de elementos imutáveis',
    'dicionário': 'Sequência de pares chave-valor',
    'print': 'Comando que tem como função a exibição de algo no monitor'}

print("Em programação temos alguns termos, entre eles estão:\n")
print(f"Variável: {glossário['variável']}.\n")
print(f"Lista: {glossário['lista']}.\n")
print(f"Tupla: {glossário['tupla']}.\n")
print(f"Dicionário: {glossário['dicionário']}.\n")
print(f"Print: {glossário['print']}.\n")
