"""
Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.
"""

# Jeito 1
print("\nJeito 1")
cubos = []
for valor in range(1, 11):
    cubos.append(valor**3)
for cubo in cubos:
    print(cubo)

# Jeito 2
print("\nJeito 2")
cubos = [valor**3 for valor in range(1, 11)]
for cubo in cubos:
    print(cubo)
