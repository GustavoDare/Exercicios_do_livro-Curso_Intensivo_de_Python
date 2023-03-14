"""
Comece com o Exercício 6.4 (página 155), em que usamos um dicionário-padrão para representar um glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de que a ordem da saída coincida com a ordem em que os pares chave-valor foram adicionados ao dicionário.
"""

# Obs.: A partir do Python 3.7 os dicionários já são ordenados, isto é, mantêm a ordem de inserção

from collections import OrderedDict

glossário = OrderedDict()
glossário = {'variável': 'Espaço na memória do computador destinado a um dado',
    'lista': 'Sequência de elemetos mutáveis durante a execução do programa',
    'tupla': 'Sequência de elementos imutáveis',
    'dicionário': 'Sequência de pares chave-valor',
    'print': 'Comando que tem como função a exibição de algo no monitor'}

glossário['função'] = ('Sequência de comandos que executa alguma tarefa e que tem um nome')
glossário['método'] = 'Função que "pertence" a um objeto instância'
glossário['conjunto'] = 'Sequência de elementos que não se repetem'
glossário['python'] = 'Linguagem de programação'
glossário['comentários'] = ('Linhas de código que tem como intuito explicar a funcionalidade do código, sendo ignorada pelo compilador')

for palavra, definição in glossário.items():
    print(f"{palavra.upper()} - {definição}")
