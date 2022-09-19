# Autor: Gustavo Daré
# Data: 25/04/2022

'''
Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3 anos de 
    idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso 
    custará 15 dólares. Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.
'''

idade = ''

while idade != 'quit':
    
    print("\nCaso queira encerrar a pesquisa digite 'quit'.")
    idade = input("Digite uma idade para saber o preço do ingresso: ")

    if idade != 'quit':
        if int(idade) < 3:
            print("Para menores de 3 anos, o ingresso é grátis.")
        elif int(idade) <= 12:
            print("Para pessoas entre 3 e 12 anos, o ingresso é R$10,00.")
        else:
            print("Para maiores de 12 anos, o ingresso é R$ 15,00.")
