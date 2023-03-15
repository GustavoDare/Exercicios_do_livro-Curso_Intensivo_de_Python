"""
Modifique o seu bloco except do Exercício 10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.
"""

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding="utf8") as file_object:
            texto = file_object.read()
            print(f"{texto}\n")
    except FileNotFoundError:
        pass

ler_arquivo('Capítulo 10\cats.txt')
ler_arquivo('Capítulo 10\dogs.txt')
