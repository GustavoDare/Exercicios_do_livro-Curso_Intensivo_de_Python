"""
Comece com seu programa do Exercício 4.1 (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.
"""

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
