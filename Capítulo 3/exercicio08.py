# Autor: Gustavo Daré
# Data: 08/04/2022

# Criar uma lista com 5 lugares, exbir a lista, exibir a lista em ordem
#     alfabética com sorted(), exibir a lista na forma original, exebir
#     a lista em ordem alfabética inversa com sorted(), exibir a lista
#     na forma original, utilizar reverse() na lista e exibí-la, repetir
#     este último, utilizar sort() na lista e exibí-la, utilizar sort()
#     na lista deixando em ordem alfabética inversa e exibí-la.

locais = ["londres", "barcelona", "nova iorque", "paris", "buenos aires"]
print(f"\nOrdem original da lista: {locais}")
print(f"Lista em ordem alfabética: {sorted(locais)}")
print(f"Lista ainda na forma original: {locais}")
print(f"Lista em ordem alfabética: {sorted(locais, reverse = True)}")
print(f"Lista ainda na forma original: {locais}")
locais.reverse()
print(f"Lista na ordem inversa: {locais}")
locais.reverse()
print(f"Lista na ordem inversa voltando ao original: {locais}")
locais.sort()
print(f"Lista em ordem alfabética permanente: {locais}")
locais.sort(reverse = True)
print(f"Lista em ordem alfabética inversa permanente: {locais}\n")
