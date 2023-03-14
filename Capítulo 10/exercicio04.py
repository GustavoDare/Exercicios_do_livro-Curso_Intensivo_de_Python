"""
Escreva um laço while que pergunte o nome aos usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e acrescente uma linha que registre a visita do usuário em um arquivo chamado guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do arquivo.
"""

print("Digite q ou quit para finalizar a inserção de nome de usuário")
while True:
    nome_usuario = input("Digite um nome de usuário: ")
    if nome_usuario.lower() == 'q' or nome_usuario.lower() == 'quit':
        break
    else:
        print(f"Welcome {nome_usuario}!")
        with open('Capítulo 10\guest_book.txt', 'a', encoding="utf8") as file_object:
            file_object.write(f'{nome_usuario}\n')
