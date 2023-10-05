import os
import sys

def find_admin_panel():
    try:
        os.system("python admin/admin.py")
    except FileNotFoundError:
        print("admin/admin.py dosyası bulunamadı.")

def send_sms():
    try:
        os.system("python sms.py")
    except FileNotFoundError:
        print("sms.py dosyası bulunamadı.")

def generate_password():
    try:
        os.system("python şifre.py")
    except FileNotFoundError:
        print("şifre.py dosyası bulunamadı.")

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
    print("      Coded By Bal.K4hin                   ")
    print("\033[0m")

while True:
    os.system("clear")
    banner()

    print("\033[0;31m[1]\033[0m Admin panelini bul")
    print("\033[0;31m[2]\033[0m SMS gönder")
    print("\033[0;31m[3]\033[0m Şifre oluştur")
    print("\033[0;31m[Q]\033[0m Çıkış")

    choice = input("Seçim yapın: ")

    if choice == "1":
        find_admin_panel()
    elif choice == "2":
        send_sms()
        sys.exit(0)
    elif choice == "3":
        generate_password()
    elif choice.lower() == "q":
        sys.exit(0)
    else:
        print("\033[0;31mGeçersiz bir seçim yaptınız. Tekrar deneyin.\033[0m")
