"""
Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.
"""

# Exercício 06
impares = list(range(1, 20, 2))
for impar in impares:
    print(impar)

print(f"Os 3 primeiros elementos da lista são: {impares[:3]}")
print(f"Os 3 elementos do meio da lista são: {impares[4:7]}")
print(f"Os 3 últimos elementos da lista são: {impares[-3:]}")
