"""
Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.
"""

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
