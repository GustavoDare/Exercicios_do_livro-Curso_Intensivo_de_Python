"""
Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e encontre alguns textos que você gostaria de analisar. Faça download dos arquivos-texto dessas obras ou copie o texto puro de seu navegador para um arquivo-texto em seu computador.
Você pode usar o método count() para descobrir quantas vezes uma palavra ou expressão aparece em uma string. Por exemplo, o código a seguir conta quantas vezes a palavra 'row' aparece em uma string:
    line = "Row, row, row your boat"
    line.count('row')
    2
    line.lower().count('row')
    3
Observe que converter a string para letras minúsculas usando lower() faz com que todas as formas da palavra que você está procurando sejam capturadas, independentemente do modo como elas estiverem grafadas.
Escreva um programa que leia os arquivos que você encontrou no Projeto Gutenberg e determine quantas vezes a palavra 'the' aparece em cada texto.
"""

with open('Capítulo 10\Little Men.txt', 'r') as file_object:
    texto = file_object.read()
    aparições = texto.lower().count('the')
    print(f"A palavra 'the' aparece {aparições} vezes no texto.")
