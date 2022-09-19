# Autor: Gustavo Daré
# Data: 21/04/2022

'''
Criar 2 listas ('usuários_atuais' e 'novos_usuários') com 5 nomes cada, sendo que 2 dos nomes devem estar presente em ambas as listas.
    Percorra a lista de novos_usuários, caso o nome já esteja na lista de usuários_atuais, exibir uma mensagem falando para colocar 
    outro nome, caso não, exibir uma mensagem de nome adicionado (não diferenciar maiúsculas de minúsculas).
'''
usuários_atuais = ["gustavo", "josé", "admin", "maria", "rita"]
novos_usuários = ["ANA", "João", "josé", "antônia", "GUSTAVO"]

for usuário in novos_usuários:
    if usuário.lower() in usuários_atuais:
        print(f"Informe outro nome, pois {usuário.title()} já existe.")
    else:
        print(f"Nome {usuário.title()} adicionado com sucesso.")
