import os
from subprocess import check_output
import sys

def find_admin_panel():
    try:
        os.system("python admin/admin.py")
    except FileNotFoundError:
        print("admin/admin.py dosyası bulunamadı.")

def run_infoga():
    try:
         domain = domain
         domain=input(" Hedef Domaini Girin: ")
         os.system("python ınf/infoga.py -d {domain} ")
    except FileNotFoundError:
     print("infoga bulunamadı!")

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

def scan_with_nmap():
    os.system("nmap/./nmap")

def run_sql_injection():
    os.system("python sqlmap/sqlmap.py")

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

while True:
    os.system("")
    banner()

    print("\033[0;31m[1]\033[0m Admin panelini bul")
    print("\033[0;31m[2]\033[0m SMS gönder")
    print("\033[0;31m[3]\033[0m Şifre oluştur")
    print("\033[0;31m[4]\033[0m Nmap taraması yap")
    print("\033[0;31m[5]\033[0m SQL Injection çalıştır")
    print("\033[0;31m[6]\033[0m Domain Mail+Ip adress")
    print("\033[0;31m[Q]\033[0m Çıkış")

    choice = input("Seçim yapın: ")

    if choice == "1":
        find_admin_panel()
    elif choice == "2":
        send_sms()
        sys.exit(0)
    elif choice == "3":
        generate_password()
    elif choice == "4":
        scan_with_nmap()
    elif choice == "5":
        run_sql_injection()
    elif choice == "6":
        run_infoga()    
    elif choice.lower() == "q":
        sys.exit(0)
    else:
        print("\033[0;31mGeçersiz bir seçim yaptınız. Tekrar deneyin.\033[0m")
