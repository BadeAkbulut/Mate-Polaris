from datetime import datetime

sinav_str=input("Sınav tarihini ve saatini şu formatta giriniz(GG-AA-YYYY HH:MM):")
sinav_tarihi=datetime.strptime(sinav_str,"%d-%m-%Y %H:%M")

simdi=datetime.now()

fark=sinav_tarihi-simdi

kalan_gun=fark.days
kalan_saat=fark.seconds//3600  #saniyeden saate çevirdik

print("-Vize Sayacı-")
print("Sınava Kalan Süre:")
print(kalan_gun,"gün",kalan_saat,"saat")


