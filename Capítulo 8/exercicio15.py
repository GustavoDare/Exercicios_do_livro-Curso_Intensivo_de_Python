# Autor: Gustavo Daré
# Data: 21/07/2022

'''
Coloque as funções do exemplo print_models.py em um arquivo separado de 
    nome printing_functions.py. Escreva uma instrução import no início 
    de print_models.py e modifique o arquivo para usar as funções 
    importadas.
'''
import exercicio15_modulo

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

exercicio15_modulo.print_models(unprinted_designs, completed_models)
exercicio15_modulo.show_completed_models(completed_models)
