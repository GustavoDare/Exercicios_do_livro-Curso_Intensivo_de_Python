# Autor: Gustavo Daré
# Data: 21/04/2022

# Crie uma lista 'usuários' com 5 nomes, sendo um deles 'admin', 
#     percorra a lista exibindo uma mensagem. "Olá admin, gostaria de
#     ver um relatório de status?", caso o usuário seja o admin e "Olá
#     'usuário', obrigado por fazer login novamente".

usuários = ["gustavo", "josé", "admin", "maria", "rita"]
for usuário in usuários:
    if usuário.lower() == 'admin':
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {usuário.title()}, obrigado por fazer login novamente.")
