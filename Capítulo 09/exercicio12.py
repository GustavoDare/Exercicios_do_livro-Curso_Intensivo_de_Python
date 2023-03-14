"""
Armazene a classe User em um módulo e as classes Privileges e Admin em um módulo separado. Em outro arquivo, crie uma instância de Admin e chame show_privileges() para mostrar que tudo continua funcionando de forma apropriada.
"""

from exercicio12_modulo2 import Admin

admin = Admin('Tais', 'Cardoso', 51, 'gerente')

admin.describe_user()
admin.privileges.show_privileges()
