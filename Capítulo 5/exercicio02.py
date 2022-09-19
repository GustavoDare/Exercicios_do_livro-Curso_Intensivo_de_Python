# Autor: Gustavo Daré
# Data: 20/04/2022

'''
Criar testes condicionais utilizando: igualdade e não igualdade para strings; a função lower(); igualdade, não igualdade, maior que,
    menor que, maior ou igual a, menor ou igual a para testes numéricos; as palavras 'and' e 'or'; e verificar se um item está e não
    está em uma lista. Obter um True e um False para cada teste.
'''

comida_preferida = "estrogonofe"
esporte_preferido = "Handebol"
idade = 21
ano_nascimento = 2000
pizzas = ["calabresa", "pepperoni", "quatro queijos", "carne seca"]

print(f"Meu esporte preferido é handebol? {esporte_preferido.lower() == 'handebol'}")
print(f"Meu esporte preferido é futebol? {esporte_preferido.lower() == 'futebol'}")
print(f"Meu esporte preferido não é handebol? {esporte_preferido.lower() != 'handebol'}")
print(f"Meu esporte preferido não é vôlei? {esporte_preferido.lower() != 'vôlei'}")
print(f"Minha idade é igual a 21? {idade == 21}")
print(f"Minha idade é igual a 25? {idade == 25}")
print(f"Minha idade é diferente de 21? {idade != 21}")
print(f"Minha idade é diferente de 25? {idade != 25}")
print(f"O número 20 é maior que 15? {20 > 15}")
print(f"O número 20 é maior que 25? {20 > 25}")
print(f"O número 83 é maior ou igual que 83? {83 >= 83}")
print(f"O número 83 é maior ou igual que 85? {83 >= 85}")
print(f"O número 20 é menor que 25? {20 < 25}")
print(f"O número 20 é menor que 15? {20 < 15}")
print(f"O número 38 é menor ou igual que 38? {38 <= 38}")
print(f"O número 38 é menor ou igual que 35? {38 <= 35}")
print(f"Nasci no ano de 2000 e tenho 21 anos? {idade == 21 and ano_nascimento == 2000}")
print(f"Nasci no ano 2000 e tenho 22 anos? {idade == 22 and ano_nascimento == 2000}")
print(f"Tenho como esporte preferido handebol ou comida preferida fruta? {esporte_preferido.lower() == 'handebol' or comida_preferida =='fruta'}")
print(f"Tenho como esporte preferido basquete e comida preferida macarrão? {esporte_preferido == 'basquete' or comida_preferida == 'macarrão'}")
print(f"Tem o sabor calabresa na lista pizzas? {'calabresa' in pizzas}")
print(f"Tem o sabor portuguesa na lista pizzas? {'portuguesa' in pizzas}")
print(f"Não tem o sabor pepperoni na lista pizzas? {'pepperoni' not in pizzas}")
print(f"Não tem o sabor portuguesa na lista pizzas? {'portuguesa' not in pizzas}")
