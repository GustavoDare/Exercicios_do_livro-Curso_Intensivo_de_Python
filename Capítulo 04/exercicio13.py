"""
Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida, use um laço for para exibir cada um dos itens do cardápio revisado.
"""

comidas = ("feijoada", "estrogonofe", "macarronada", "lasanha", "arroz")
print("\nO cardápio é:")
for comida in comidas:
    print(comida.title())

comidas = ("creme de milho", "estrogonofe", "macarronada", "lasanha", "salada")
print("\nO cardápio modificado é:")
for comida in comidas:
    print(comida.title())
