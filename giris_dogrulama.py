import re

sifre = input("Bir şifre belirleyin: ")

sifre_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'

if re.match(sifre_regex, sifre):
    print("Şifre güçlü. Onaylandı.")
else:
    print(" Şifre zayıf!")
    print("Şifre en az 1 büyük harf, 1 rakam ve 1 özel karakter içermelidir.")
    
    


