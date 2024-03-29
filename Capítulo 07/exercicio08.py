# Autor: Gustavo Daré
# Data: 27/04/2022

'''
Crie uma lista chamada 'sandwich_orders' e a preencha com os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada 
    'finished_sandwiches'. Percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido, por exemplo,
    'Preparei seu sanduíchede atum'. À medida que cada sanduíche for preparado, transfira-o para a lista de sanduíches prontos. Depois
    que todos os sanduíches estiverem prontos, mostre uma mensagem que liste cada sanduíche preparado.
'''

sandwich_orders = ['x-burguer', 'x-bacon', 'x-salada', 'x-tudo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Preparei seu {sandwich}.")
    finished_sandwiches.append(sandwich)

print(f"\nOs sanduíches finalizados foram:")
for sandwich in finished_sandwiches:
    print(f"    {sandwich}")
