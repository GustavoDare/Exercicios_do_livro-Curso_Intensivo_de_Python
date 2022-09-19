# Autor: Gustavo Daré
# Data: 21/07/2022

'''
Usando um programa que você tenha escrito e que contenha uma única função, armazene essa função em um arquivo separado. Importe a função 
    para o arquivo principal de seu programa e chame-a usando cada uma das seguintes abordagens:
        import nome_do_módulo
        from nome_do_módulo import nome_da_função
        from nome_do_módulo import nome_da_função as nf
        import nome_do_módulo as nm
        from nome_do_módulo import *
'''

# As abordagens serão feitas nos arquivos exercicio16_1; exercicio16_2;
#    exercicio16_3; exercicio16_4;exercicio16_5, respectivamente.

def show_magicians(magicos):
    """Função retirada do exercício 9 do capítulo 8"""
    for magico in magicos:
        print(magico.title())
