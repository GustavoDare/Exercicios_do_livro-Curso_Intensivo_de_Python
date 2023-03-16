"""
A última listagem de remember_me.py supõe que o usuário já forneceu seu nome ou que o programa está executando pela primeira vez. Devemos modificá-lo para o caso de o usuário atual não ser a pessoa que usou o programa pela última vez.
Antes de exibir uma mensagem de boas-vindas de volta em greet_user(), pergunte ao usuário se seu nome está correto. Se não estiver, chame get_new_username() para obter o nome correto.
"""

import json

def get_stored_username():
    filename = "Capítulo 10/username.json"
    try:
        with open(filename, 'r', encoding="utf8") as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
         None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = "Capítulo 10/username.json"
    with open(filename, 'w', encoding="utf8") as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        while True:
            answer = input(f"Is your name {username}? (Yes/No) ")
            if answer.lower() == "yes" or answer.lower() == "y":
                print("Welcome back, " + username + "!")
                break
            elif answer.lower() == "no" or answer.lower() == "n":
                username = get_new_username()
                print("We'll remember you when you come back, " + username + "!")
                break
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")        

greet_user()
