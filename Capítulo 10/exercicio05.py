"""
Escreva um laço while que pergunte às pessoas por que elas gostam de programação. Sempre que alguém fornecer um motivo, acrescente-o em um arquivo que armazene todas as respostas.
"""

print("Digite q ou quit para parar de responder.")
while True:
    resposta = input("Porque você gosta de programação? ")
    if resposta.lower() == 'q' or resposta.lower() == 'quit':
        break
    else:
        with open('Capítulo 10\ ansers.txt', 'a', encoding="utf8") as file_object:
            file_object.write(f'{resposta}\n')
