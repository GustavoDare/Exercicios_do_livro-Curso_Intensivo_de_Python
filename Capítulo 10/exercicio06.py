"""
Um problema comum quando pedir entradas numéricas ocorre quando as pessoas fornecem texto no lugar de números. Ao tentar converter a entrada para um int, você obterá um TypeError. Escreva um programa que peça dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso algum dos valores de entrada não seja um número e apresente uma mensagem de erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite um texto no lugar de um número.
"""

def tratamento_erro(valor):
    try:
        valor = float(valor)
    except ValueError:
        print("É necessário digitar um número para efetuar a operação")
        return 0
    else:
        return valor

valor1 = input("Digite o primeiro número: ")
valor1 = tratamento_erro(valor1)
valor2 = input("Digite o segundo número: ")
valor2 = tratamento_erro(valor2)
soma = valor1 + valor2
print(f"A soma dos valores {valor1} e {valor2} é: {soma}")
