"""
Use uma list comprehension para gerar uma lista dos dez primeiros cubos.
"""

cubos = [valor**3 for valor in range(1, 11)]
for cubo in cubos:
    print(cubo)
