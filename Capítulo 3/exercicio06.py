# Autor: Gustavo Daré
# Data: 07/04/2022

# Modificar o exercício 4 do capítulo 3 adicionando mais 3 convidados 
#     utilizando insert() e append()
# Colocar um convidado no início, outro no meio e outro no final da 
#     lista e exibir os convites novamente

convidados = ["Albert Einstein", "Marie Curie", "Issac Newton"]
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[1]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[2]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")

print("Pelo fato de ter achado uma mesa maior, irei acrescentar 3 convidados para o jantar")

convidados.insert(0, "Niels Böhr")
convidados.insert(2, "Madona")
convidados.append("Michael Jackson")
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[1]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[2]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[3]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[4]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[5]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")