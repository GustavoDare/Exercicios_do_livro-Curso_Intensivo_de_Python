# Autor: Gustavo Daré
# Data: 08/04/2022

# Reutilizar o programa do exercício 4 do capítulo 3 para acrescentar uma mensagem falando quantos convidados 
#   estão na lista, usando o método 'len()'

convidados = ["Albert Einstein", "Marie Curie", "Issac Newton"]
print(f"\nPrezado {convidados[0]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.")
print(f"Prezada {convidados[1]}, gostaria de convidá-la para jantar comigo e mais alguns convidados.")
print(f"Prezado {convidados[2]}, gostaria de convidá-lo para jantar comigo e mais alguns convidados.\n")

print(f"Estão sendo convidados {len(convidados)} pessoas para o jantar.\n")