x=float(input("İlk sayıyı giriniz:"))
y=float(input("İkinci sayıyı giriniz:"))

toplam=x+y
fark=x-y
carpim=x*y

#Bölüm için paydanın sıfır olup olmadığını kontrol etmemiz lazım.
if y!=0:
    bolum=x/y
    bolum_kontrol=f"{bolum}"
else:
    bolum_kontrol="Tanımsız"

print("Çıktılar:")
print("Toplam=",toplam)
print("Fark=",fark)
print("Çarpım=",carpim)
print("Bölüm=",bolum_kontrol)


