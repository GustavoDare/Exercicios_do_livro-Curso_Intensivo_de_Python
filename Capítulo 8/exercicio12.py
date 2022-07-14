# Autor: Gustavo Daré
# Data: 13/07/2022

'''
Escreva uma função que aceite uma lista de itens que uma pessoa quer em 
    um sanduíche. A função deve ter um parâmetro que agrupe tantos itens
    quantos forem fornecidos pela chamada da função e deve apresentar um
    resumo do sanduíche pedido. Chame a função três vezes usando um 
    número diferente de argumentos a cada vez.
'''

def fazer_sanduiche(*ingredientes):
    print("\nO sanduíche pedido possui os seguintes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.title()};")

fazer_sanduiche('salame', 'picles', 'bacon')
fazer_sanduiche('bacon', 'queijo', 'hambúrguer', 'alface', 'tomate')
fazer_sanduiche('hambúrguer', 'queijo')
