# Autor: Gustavo Daré
# Data: 08/04/2022

# Criar uma lista com nome de países e utilizar todas as funções apresentadas no capítulo

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
