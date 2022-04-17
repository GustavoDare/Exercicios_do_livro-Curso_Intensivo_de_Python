# Autor: Gustavo Daré
# Data: 17/04/2022

# Copiar o exercício 1 do capítulo 4, fazer uma cópia da lista, adicionar uma 
#     pizza na lista original e outra, diferente, na cópia, e exibir as duas 
#     listas provando que são listas diferentes

pizzas = ["calabresa", "carne seca", "brócolis com bacon"]
for pizza in pizzas:
    print(f"Gosto de pizza de {pizza.title()}.")
print("\nEu realmente adoro pizza.\n")

pizzas_amigo = pizzas[:]

pizzas.append("lombinho")
pizzas_amigo.append("quatro queijos")

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza.title())
print("\nAs pizzas favoritas do meu amigo são:")
for pizza_amigo in pizzas_amigo:
    print(pizza_amigo.title())
