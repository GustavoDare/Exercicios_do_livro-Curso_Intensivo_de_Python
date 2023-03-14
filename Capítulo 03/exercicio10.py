"""
Pensa em algo que você poderia armazenar em uma lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma lista contendo esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.
"""

paises = ["brasil", "argentina", "estados unidos", "chile", "portugal", "itália"]

print(f"\nLista original: {paises}")
print(f"Acessando o 2 item da lista: {paises[1]}")

paises[1] = "colômbia"
print(f"Alterando o 2 item dessa lista: {paises}")

paises.append("alemanha")
print(f"Acrescentando um país no final da lista {paises}")

paises.insert(3, "japão")
print(f"Acrescentando um país no índice 3: {paises}")
print(f"O tamanho da lista atual é de: {len(paises)}")

del paises[2]
print(f"Deletando o terceiro pais da lista: {paises}")

paises.remove("chile")
print(f"Removendo o pais 'chile' da lista: {paises}")
print(f"Alterando temporáriamente a lista em ordem alfabética: {sorted(paises)}")
print(f"Lista na mesma ordem após remover o 'chile': {paises}")

paises.reverse()
print(f"Lista em ordem inversa: {paises}")

paises.sort()
print(f"Lista em ordem alfabética permanente: {paises}")

pais_excluido = paises.pop()
print(f"Lista com o pais '{pais_excluido}' excluido utilizando pop(): {paises}\n")
