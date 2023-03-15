"""
Coloque o código do Exercício 10.6 em um laço while para que o usuário possa continuar fornecendo números, mesmo se cometerem um erro e digitarem um texto no lugar de um número.
"""

def tratamento_erro(valor):
    try:
        valor = float(valor)
    except ValueError:
        print("É necessário digitar um número para efetuar a operação")
        return 0
    else:
        return valor

soma = 0
print("Digite q ou quit para ver a soma dos números digitados")
while True:
    numero = input("Digite o primeiro número: ")
    if numero.lower() == 'q' or numero.lower() == 'quit':
        break
    else:
        numero = tratamento_erro(numero)
        soma += numero
    
print(f"A soma dos números digitados é: {soma}")
