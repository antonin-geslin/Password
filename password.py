import re
import hashlib
import json


def check_password(password):
    bool = True
    SpecialSym =['$', '@', '#', '%', '!', '/', '=', '.', ':', '+']
    if (len(password) < 8):
        print("Le mot de passe trop court")
        bool = False
    if not any(char.isdigit() for char in password):
        print("Le mot de passe doit contenir au moins un chiffre")
        bool = False
    if not any(char.isupper() for char in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule")
        bool = False
    if not any(char.islower() for char in password):
        print("Le mot de passe doit contenir au moins une lettre minuscule")
        bool = False
    if not any(char in SpecialSym for char in password):
        print("Le mot de passe doit contenir au moins un caractère spécial")
        bool = False
    
    if bool == False:
        password = input("Entrez votre mot de passe : ")
        check_password(password)
    else:
        print("Mot de passe sécurisé")
    return(password)

def crypt(password):
    hashed = hashlib.sha256(str.encode(password)).hexdigest()
    print(hashed)
    return(hashed)

def write(compte, password):
    entry = {
                'compte' : str(compte),
                'mot de passe' : str(password),
            }
    with open('password/password.json', 'r') as file:
        data = json.load(file)

    data.append(entry)

    with open('password/password.json', 'w') as file:
        json.dump(data, file)

def read():

    with open('password/password.json') as file:
        json_object = json.load(file)
    print(json_object)

         


def main():
    password = input("Entrez votre mot de passe : ")
    password = crypt(check_password(password))
    print("\n")
    question = input("Voulez vous enregistrer votre mot de passe sécurisé dans un fichier json ? y or n : ")
    if question == "y":
        print("\n")
        compte = input("Rensignez le compte associé à votre mot de passe : ")
        write(compte, password)
        print("\n")
        read()
    
main()