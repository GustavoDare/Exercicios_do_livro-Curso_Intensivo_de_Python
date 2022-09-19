# Autor: Gustavo Daré
# Data: 04/04/2022

# Exibir um nome retirando os espaços em suas extremidades (direita, esquerda e ambas)

nome = "\n\tGustavo Daré  \n"

print(f"Nome com espaços em branco: {nome}")
print(f"Nome sem espaços em branco do lado direito: {nome.rstrip()}")
print(f"Nome sem espaços em branco do lado esquerdo: {nome.lstrip()}")
print(f"Nome sem espaços em branco: {nome.strip()}\n")
