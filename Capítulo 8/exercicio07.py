# Autor: Gustavo Daré
# Data: 08/06/2022

'''
Escreva uma função chamada make_album() que construa um dicionário descrevendo um álbum musical. A função deve aceitar o nome de um 
    artista e o título de um álbum e deve devolver um dicionário contendo essas duas informações. Use a função para criar três dicionários 
    que representem álbuns diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão armazenando as informações do 
    álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o número de faixas em um álbum. Se a linha que fizer a chamada 
    incluir um valor para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo menos uma nova chamada da função 
    incluindo o número de faixas em um álbum.
'''

def make_album(artista, titulo, faixas=''):
    if faixas:
        album = {'artista': artista.title(), 'titulo': titulo.title(), 'n_faixas': faixas}
    else:
        album = {'artista': artista.title(), 'titulo': titulo.title()}
    return album

album1 = make_album('michael jackson', 'thriller')
album2 = make_album('taylor swift', '1989', 13)
album3 = make_album('dua lipa', 'future nostalgia', 11)

print(album1)
print(album2)
print(album3)
