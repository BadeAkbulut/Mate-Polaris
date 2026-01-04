#lvl1_bozuk_veri için

import re

with open("lvl1_bozuk_veri.txt", "r", encoding="utf-8") as file:
    veri = file.read()

email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
telefon_regex = r'\b(?:\+90|0)?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b'

emailler = re.findall(email_regex, veri)
telefonlar = re.findall(telefon_regex, veri)

with open("lvl1_temiz_rehber.txt", "w", encoding="utf-8") as out:
    for e in emailler:
        out.write(e + "\n")
    for t in telefonlar:
        out.write(t + "\n")

print("lvl1_temiz_rehber.txt oluşturuldu ✅")


#lvl2_bozuk_veri için

import re

with open("lvl2_bozuk_veri.txt", "r", encoding="utf-8") as file:
    veri = file.read()

email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
telefon_regex = r'\b(?:\+90|0)?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b'

emailler = re.findall(email_regex, veri)
telefonlar = re.findall(telefon_regex, veri)

with open("lvl2_temiz_rehber.txt", "w", encoding="utf-8") as out:
    for e in emailler:
        out.write(e + "\n")
    for t in telefonlar:
        out.write(t + "\n")

print("lvl2_temiz_rehber.txt oluşturuldu ✅")

