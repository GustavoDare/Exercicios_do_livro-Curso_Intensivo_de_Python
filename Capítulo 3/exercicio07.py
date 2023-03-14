"""
Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.
"""

convidados = ["Albert Einstein", "Marie Curie", "Issac Newton"]
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[1]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[2]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")

print("Pelo fato de ter achado uma mesa maior, irei acrescentar 3 convidados para o jantar.")

convidados.insert(0, "Niels Böhr")
convidados.insert(2, "Madona")
convidados.append("Michael Jackson")

print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[1]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[2]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[3]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[4]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[5]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")

print("Infelizmente a mesa não chegará a tempo e, portanto, só dará para convidar duas pessoas para o jantar.")

removido = convidados.pop(0)
print(f"\nPrezado {removido}, sinto muito por não poder convidá-lo para o jantar.")
removido = convidados.pop(0)
print(f"Prezado {removido}, sinto muito por não poder convidá-lo para o jantar.")
removido = convidados.pop(1)
print(f"Prezada {removido}, sinto muito por não poder convidá-la para o jantar.")
removido = convidados.pop(1)
print(f"Prezado {removido}, sinto muito por não poder convidá-lo para o jantar.")

print(f"\nPrezada {convidados[0]}, gostaria de informar que o convite continua para a senhora.")
print(f"Prezado {convidados[1]}, gostaria de informar que o convite continua para o senhor.\n")
del convidados[0]
del convidados[0]

print(f"A lista de convidados após retirado os convidados: {convidados}\n")
