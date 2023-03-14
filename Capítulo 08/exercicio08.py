# Autor: Gustavo Daré
# Data: 08/06/2022

'''
Comece com o seu programa do Exercício 8.7. Escreva um laço while que permita aos usuários fornecer o nome de um artista e o título de 
    um álbum. Depois que tiver essas informações, chame make_album() com as entradas do usuário e apresente o dicionário criado. Lembre-se 
    de incluir um valor de saída no laço while.
'''

def make_album(artista, titulo):
    album = {'artista': artista.title(), 'titulo': titulo.title()}
    return album

albuns = []
print("REGISTRO DE ÁLBUNS\n")
while True:
    print("Caso não queira registrar mais nenhum álbum digite: 'OK'")
    artista = input("Informe o nome do artista: ")
    if artista.upper() == 'OK':
        break
    titulo = input("Informe o título do álbum: ")
    albuns.append(make_album(artista, titulo))

for album in albuns:
    print(album)
