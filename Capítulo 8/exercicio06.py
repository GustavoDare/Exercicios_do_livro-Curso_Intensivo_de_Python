# Autor: Gustavo Daré
# Data: 08/06/2022

'''
Escreva uma função chamada "city_country()" que aceite o nome de uma 
    cidade e seu país. A função deve devolver uma string formatada 
    assim:  "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o 
    valor devolvido.
'''

def city_coutry(cidade_país):
    for pais, cidade in cidade_país.items():
        print(f"{pais.title()}, {cidade.title()}.")

cidade_pais = {'brasília':'brasil', 'berlim':'alemanha', 
                'buenos aires':'argentina'}
city_coutry(cidade_pais)
