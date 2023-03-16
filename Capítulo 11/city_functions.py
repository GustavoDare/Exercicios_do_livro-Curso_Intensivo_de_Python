# Função exigida no exercício 01
def localidade(cidade, pais):
    localidade = f"{cidade.title()}, {pais.title()}"
    return localidade

# Função exigida no exercício 02
def localidade_modificada(cidade, pais, populacao=''):
    if populacao:
        localidade = f"{cidade.title()}, {pais.title()} - população {populacao}"
    else:
        localidade = f"{cidade.title()}, {pais.title()}"
    return localidade
