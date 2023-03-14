"""
Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de remoção de espaços: lstrip(), rstrip() e strip().
"""

nome = "\n\tGustavo Daré  \n"

print(f"Nome com espaços em branco: {nome}")
print(f"Nome sem espaços em branco do lado direito: {nome.rstrip()}")
print(f"Nome sem espaços em branco do lado esquerdo: {nome.lstrip()}")
print(f"Nome sem espaços em branco: {nome.strip()}\n")
