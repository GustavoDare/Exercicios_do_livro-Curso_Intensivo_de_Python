"""
Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o conteúdo do arquivo na tela. Coloque seu código em um bloco try-except para capturar o erro FileNotFound e apresente uma mensagem simpática caso o arquivo não esteja presente. Mova um dos arquivos para um local diferente de seu sistema e garanta que o código no bloco except seja executado de forma apropriada.
"""

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding="utf8") as file_object:
            texto = file_object.read()
            print(f"{texto}\n")
    except FileNotFoundError:
        print("Não foi possível encontrar este arquivo.")

ler_arquivo('Capítulo 10\cats.txt')
ler_arquivo('Capítulo 10\dogs.txt')
