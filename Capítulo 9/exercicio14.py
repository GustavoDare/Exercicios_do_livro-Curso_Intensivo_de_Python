"""
O módulo random contém funções que geram números aleatórios de várias maneiras. A função randint() devolve um inteiro no intervalo especificado por você. O código a seguir devolve um número entre 1 e 6: 
    from random import randint 
    x = randint(1, 6)
Crie uma classe Die com um atributo chamado sides, cujo valor default é 6. Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e o número de lados do dado. Crie um dado de seis lados e lance-o dez vezes.
Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes.
"""

from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, lançamentos):
        print(f"\nPara o dado de {self.sides} faces foram sorteados os números: ")
        for vezes in range(0, lançamentos):
            x = randint(1, self.sides)
            print(x, end='  ')

dado_6faces = Die()
dado_6faces.roll_die(10)

dado_10faces = Die(10)
dado_10faces.roll_die(10)

dado_20faces = Die(20)
dado_20faces.roll_die(10)
