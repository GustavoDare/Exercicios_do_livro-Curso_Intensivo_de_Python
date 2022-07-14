# Autor: Gustavo Daré
# Data: 13/07/2022

'''
Comece com uma cópia de user_profile.py, da página 210. Crie um perfil 
    seu chamando build_profile(), usando seu primeiro nome e o 
    sobrenome, além de três outros pares chave-valor que o descrevam.
'''

def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um
usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',
                                field='physics')
print(user_profile)

meu_perfil = build_profile('gustavo', 'daré', favorite_food='lasanha',
                        favorite_color='vermelho', favorite_sport='handebol')

print("\nImpressão 1: ")
for chave, valor in meu_perfil.items():
    print(f"{chave.title()}: {valor.title()}")
print("\nImpressão 2: ")
print(meu_perfil)
