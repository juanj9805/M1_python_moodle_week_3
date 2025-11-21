import csv
login_attempts = 3

from colorama import Fore, Style, init

init()

with open("login.csv", "r") as  archivo:
    attempts = 3
    lector = csv.reader(archivo)
    loged = False
    while attempts != 0 :
        login_email_info = input(Fore.LIGHTBLACK_EX + "Email address: ")
        login_password_info = input(Fore.LIGHTBLACK_EX + "Password: ")
        for fila in lector:
            if fila[1] == login_email_info and fila[2] == login_password_info:
                attempts = 0
                loged = True
                break
        else:
            attempts -= 1
            print(Fore.YELLOW + f"Something went wrong, you have {attempts} attempts more")
    if loged == False:
        print(Fore.RED + "You must reset the password")
    elif loged == True:
        print(Fore.GREEN + f"Welcome {fila[0]}")

