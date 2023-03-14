"""
Você pode usar o método replace() para substituir qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rápido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
   message = "I really like dogs."
   message.replace('dog', 'cat')
   'I really like cats.'
Leia cada linha do arquivo learning_python.txt que você acabou de criar e substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre cada linha modificada na tela.
"""

with open('Capítulo 10\learning_python.txt', 'r', encoding="utf8") as file_object:
    linhas_texto = file_object.readlines()

for linha_texto in linhas_texto:
    linha_texto = linha_texto.replace(" Python ", " C ")
    print(linha_texto.rstrip())
