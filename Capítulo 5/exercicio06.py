# Autor: Gustavo Daré
# Data: 21/04/2022

'''
Escrever uma cadeia if-elif-else para uma variável idade, caso o valor seja: menor que 2 - bebê, maior ou igual que 2 e menor 
    que 4 - criança, maior ou igual que 4 e menor que 13 - garoto(a), maior ou igual que 13 e menos que 20 - adolescente, maior 
    ou igual que 20 e menos que 65 - adulto, 65 ou mais - idoso.
'''

idade = 45
if idade < 2:
    print("Você é bebê.")
elif idade < 4:
    print("Você é criança.")
elif idade < 13:
    print("Você é um(a) garoto(a).")
elif idade < 20:
    print("Você é adolescente.")
elif idade < 65:
    print("Você é adulto(a)")
else:
    print("Você é idoso(a).")
