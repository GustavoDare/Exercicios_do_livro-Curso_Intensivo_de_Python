# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três lugares 
    favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante, peça a alguns amigos que nomeiem alguns de 
    seus lugares favoritos. Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.
'''

favorite_place = {'gabriela': ['ilha sul', 'paris', 'bora bora'], 'felipe': ['tahiti', 'maui'], 'laura': ['londres', 'roma', 'phuket']}

for nome, lugares in favorite_place.items():
    if len(lugares) == 1:
        print(f"O lugar favorito do(a) {nome.title()} é:")
    else:
        print(f"Os lugares favoritos do(a) {nome.title()} são:")
        
    for lugar in lugares:
        print(f"    {lugar.title()}")
