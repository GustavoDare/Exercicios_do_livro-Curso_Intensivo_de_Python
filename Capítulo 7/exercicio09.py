# Autor: Gustavo Daré
# Data: 27/04/2022

'''
Usando a lista 'sandwich_orders' do Exercício 8, garanta que o 
    sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
    Acrescente um código próximo ao início de seu programa para exibir 
    uma mensagem informando que a lanchonete está sem pastrami e, então,
    use um laço while para remover todas as ocorrências de 'pastrami' em 
    'sandwich_orders'. Garanta que nenhum sanduíche de pastrami acabe em 
    'finished_sandwiches'.
'''

sandwich_orders = ['x-burguer', 'pastrami', 'pastrami','x-bacon', 'x-salada', 
    'x-tudo', 'pastrami']
finished_sandwiches = []

print(f"Os sanduíches pedidos são: {sandwich_orders}.")
print("Porém a lanchonete hoje está sem pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Preparei seu {sandwich}.")
    finished_sandwiches.append(sandwich)

print(f"\nOs sanduíches finalizados foram:")
for sandwich in finished_sandwiches:
    print(f"    {sandwich}")
