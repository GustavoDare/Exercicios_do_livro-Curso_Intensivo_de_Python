# Autor: Gustavo Daré
# Data: 22/04/2022

# Utilizando o exercício 3 do capítulo 6, ao invés das funções prints 
#     utilizar um laço que percorra as chaves e valores para exibí-los 
#     na tela. Ao final, acrescentar mais 5 termos e exibí-los de novo.

glossário = {'variável': 'Espaço na memória do computador destinado a um dado',
    'lista': 'Sequência de elemetos mutáveis durante a execução do programa',
    'tupla': 'Sequência de elementos imutáveis',
    'dicionário': 'Sequência de pares chave-valor',
    'print': 'Comando que tem como função a exibição de algo no monitor'}

print("Em programação temos alguns termos, entre eles estão:\n")
for termo, definição in glossário.items():
    print(f"{termo.title()}: {definição}.\n")

glossário['função'] = ('Sequência de comandos que executa alguma tarefa e que '
    'tem um nome')
glossário['método'] = 'Função que "pertence" a um objeto instância'
glossário['conjunto'] = 'Sequência de elementos que não se repetem'
glossário['python'] = 'Linguagem de programação'
glossário['comentários'] = ('Linhas de código que tem como intuito explicar a '
    'funcionalidade do código, sendo ignorada pelo compilador')

print("Em programação temos alguns termos, entre eles estão:\n")
for termo, definição in glossário.items():
    print(f"{termo.title()}: {definição}.\n")
