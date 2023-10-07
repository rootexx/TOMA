import random
import string
import os

def banner():
     print("\033[0;31m")
     print("########::'#######::'##::::'##::::'###::::")
     print("   ##..::'##.... ##: ###::'###:::'## ##:::")
     print("   ##:::: ##:::: ##: ####'####::'##:. ##::")
     print("   ##:::: ##:::: ##: ## ### ##:'##:::. ##:")
     print("   ##:::: ##:::: ##: ##. #: ##: #########:")
     print("   ##:::: ##:::: ##: ##:.:: ##: ##.... ##:")
     print("   ##::::. #######:: ##:::: ##: ##:::: ##:")
     print("   ..::::::.......:::..:::::..::..:::::..::")
     print("\033[0m")
     banner()
     

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    os.system("")
    banner()
    try:
        length = int(input("Şifre uzunluğunu girin: "))
        password = generate_password(length)
        print("Oluşturulan Şifre:", password)
        break
    except ValueError:
        print("Geçersiz uzunluk. Lütfen bir tam sayı girin.")
