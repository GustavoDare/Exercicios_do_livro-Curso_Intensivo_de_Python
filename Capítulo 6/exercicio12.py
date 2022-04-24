# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Estamos trabalhando agora com exemplos complexos o 
    bastante para poderem ser estendidos de várias maneiras. Use um dos
    programas de exemplo deste capítulo e estenda-o acrescentando novas
    chaves e valores, alterando o contexto do programa ou melhorando a
    formatação da saída.
'''

# Alterando o exercício 3 do capítulo 6
glossário = {'variável': 'Espaço na memória do computador destinado a um dado',
    'lista': 'Sequência de elemetos mutáveis durante a execução do programa',
    'tupla': 'Sequência de elementos imutáveis',
    'dicionário': 'Sequência de pares chave-valor',
    'print': 'Comando que tem como função a exibição de algo no monitor'}
    
glossário['método'] = 'Função que "pertence" a um objeto instância'
glossário['conjunto'] = 'Sequência de elementos que não se repetem'

print("Em programação temos alguns termos, entre eles estão:\n")
for termo, definicao in  glossário.items():
    print(f"{termo.title()}: {definicao}.\n")

