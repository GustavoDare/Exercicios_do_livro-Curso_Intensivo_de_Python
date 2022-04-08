# Autor: Gustavo Daré
# Data: 07/04/2022

# Modificar o exercício 6 do capítulo 3: Manter apenas 2 convidados, mandando mensagens de desculpas aos 
#     que foram retirados e reafirmando o convite aos dois que sobraram. No final, deletar esses dois convidados
#     e mostrar que a lista atual está vazia.

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
