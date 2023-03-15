"""
Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.
"""

# Jeito 1
print(f"\nJeito 1")
multiplos_de_3 = list(range(3, 31, 3))
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)

# Jeito 2
print(f"\nJeito 2")
multiplos_de_3 = []
for valor in range(1, 11):
    multiplos_de_3.append(valor*3)
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)

# Jeito 3
print(f"\nJeito 3")
multiplos_de_3 = [valor*3 for valor in range(1, 11)]
for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)
