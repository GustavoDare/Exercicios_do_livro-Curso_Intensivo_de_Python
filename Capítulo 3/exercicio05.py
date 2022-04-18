# Autor: Gustavo Daré
# Data: 07/04/2022

# Modificar o exercício 4 do capítulo 3 retirando e acrescentando outro 
#     nome na listas de convidados, e exibir o motivo do convidado ser 
#     retirado e enviar novamente os convites aos convidados

convidados = ["Albert Einstein", "Marie Curie", "Issac Newton"]
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[1]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[2]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")

compromissado = convidados.pop(0)
print(f"Infelizmente, {compromissado} terá uma reunião e não poderá comparecer.")

convidados.insert(0, "Niels Böhr")
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[1]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[2]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")
