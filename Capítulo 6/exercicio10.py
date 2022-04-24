# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Modifique o seu programa do Exercício 6.2 (página 147) para que cada 
    pessoa possa ter mais de um número favorito. Em seguida, apresente 
    o nome de cada pessoa, juntamente com seus números favoritos.
'''

numeros_favoritos = {'maria': [5], 'gustavo': [7, 27], 'josé': [21, 45, 97],
    'joana': [5, 11], 'lucas': [10]}

for nome, numeros in numeros_favoritos.items():
    if len(numeros) == 1:
        print(f"O número favortio do(a) {nome.title()} é:")

    else:
        print(f"Os números favoritos do(a) {nome.title()} são:")
        
    for numero in numeros:
        print(f"    {numero}")
