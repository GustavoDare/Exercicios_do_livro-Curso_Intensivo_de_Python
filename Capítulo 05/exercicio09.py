# Autor: Gustavo Daré
# Data: 21/04/2022

'''
Utilizando o código do exercício 8 do capítulo 5, acrescente um if para garantir que a lista não esteja vazia, caso esteja vazia exiba a mensagem "Precisamos encontrar alguns funcionários!". Retire todos os nomes da lista para conferir se está funcionando.
'''

usuários = []
if usuários:
    for usuário in usuários:
        if usuário.lower() == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {usuário}, obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns funcionários!")
