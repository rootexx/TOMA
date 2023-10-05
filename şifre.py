import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Şifre uzunluğunu girin: "))
        password = generate_password(length)
        print("Oluşturulan Şifre:", password)
        break
    except ValueError:
        print("Geçersiz uzunluk. Lütfen bir tam sayı girin.")
