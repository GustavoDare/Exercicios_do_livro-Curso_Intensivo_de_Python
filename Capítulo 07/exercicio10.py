# Autor: Gustavo Daré
# Data: 27/04/2022

'''
Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários. Escreva um prompt semelhante a este: 
    'Se pudesse visitar um lugar do mundo, para onde você iria?' Inclua um bloco de código que apresente os resultados da enquete.
'''

lugares = {}
continuar = True

print("\nENQUETE SOBRE AS FÉRIAS DOS SONHOS!")

while continuar:
    usuario = input("\nQual o seu nome: ")
    lugar = input("Se você pudesse visitar um lugar no mundo, para onde você iria? ")
    
    lugares[usuario] = lugar
    resposta = input ("Você deseja continuar a enquete? ")

    if resposta.lower() == 'não' or resposta.lower() == 'nao':
        continuar = False

print("\nOs resultados da enquete são:")
for usuario, lugar in lugares.items():
    print(f"O lugar do sonho escolhido pelo(a) {usuario.title()} foi: {lugar.title()}.")
