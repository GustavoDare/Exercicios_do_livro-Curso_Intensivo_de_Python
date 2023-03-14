"""
Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
"""

locais = ["londres", "barcelona", "nova iorque", "paris", "buenos aires"]
print(f"\nOrdem original da lista: {locais}")
print(f"Lista em ordem alfabética: {sorted(locais)}")
print(f"Lista ainda na forma original: {locais}")
print(f"Lista em ordem alfabética: {sorted(locais, reverse=True)}")
print(f"Lista ainda na forma original: {locais}")
locais.reverse()
print(f"Lista na ordem inversa: {locais}")
locais.reverse()
print(f"Lista na ordem inversa voltando ao original: {locais}")
locais.sort()
print(f"Lista em ordem alfabética permanente: {locais}")
locais.sort(reverse=True)
print(f"Lista em ordem alfabética inversa permanente: {locais}\n")
