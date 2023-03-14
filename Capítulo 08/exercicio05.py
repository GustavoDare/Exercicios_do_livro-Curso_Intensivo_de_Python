# Autor: Gustavo Daré
# Data: 15/05/2022

'''
Escreva uma função chamada "describe_city()" que aceite o nome de uma cidade e seu país. A função deve exibir uma frase simples, como 
    "Reykjavik está localizada na Islândia". Forneça um valor default ao parâmetro que representa o país. Chame sua função para três 
    cidades diferentes em que pelo menos uma delas não esteja no país default.
'''

def describe_city(cidade, país = "Brasil"):
    print(f"{cidade.title()} está localizada no(a) {país.title()}.\n")

describe_city("São Paulo")
describe_city("Berlim", "alemanha")
describe_city("rio de janeiro")
