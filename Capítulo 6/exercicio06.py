# Autor: Gustavo Daré
# Data: 22/04/2022

'''
Utilize o código em 'favorite_languages.py' (página 150).
Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário 
    e outras que não estão.
Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes
    por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.
'''

linguagem_favorita = {
    'jean': 'python',
    'sara': 'c',
    'eduardo': 'ruby',
    'felipe': 'python',
}

pessoas = ['gustavo', 'jean', 'laura', 'ana', 'eduardo']

for pessoa in pessoas:
    if pessoa in linguagem_favorita.keys():
        print(f"Obrigado por responder a enquete, {pessoa.title()}.")
    else:
        print(f"Olá {pessoa.title()}, gostaria de convidá-lo(a) a respoder a enquete sobre qual é sua linguagem de programação favorita.")
