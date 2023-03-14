# Autor: Gustavo Daré
# Data: 13/07/2022

'''
Escreva uma função que armazene informações sobre um carro em um dicionário. A função sempre deve receber o nome de um fabricante e um 
    modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
Chame a função com as informações necessárias e dois outros pares nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser 
    apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Mostre o dicionário devolvido para garantir que todas as informações foram armazenadas corretamente.
'''

def make_car(fabricante, modelo, **adicionais):
    car = {}
    car['fabricante'] = fabricante
    car['modelo'] = modelo
    for chave, valor in adicionais.items():
        car[chave] = valor
    return car

car1 = make_car('suburu', 'outback', color='blue', tow_package=True)
car2 = make_car('ferrari', 'F8', color='red', potency=720)
car3 = make_car('audi', 'A4', price=295000, size='médio')

print(f"Especificações do carro 1:\n{car1}")
print(f"Especificações do carro 1:\n{car2}")
print(f"Especificações do carro 1:\n{car3}")
