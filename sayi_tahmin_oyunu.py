import random

hedef=random.randint(1,100)

print("Sayı tahmin oyununa hoş geldin!")
print("1 ile 100 arasında bir sayı tuttum.Tahmin etmeyi dene.\n")

while True:
    tahmin=int(input("Tahmin:"))

    if tahmin<hedef:
        print("Yukarı çık")
    elif tahmin>hedef:
        print("Aşağı in")
    else:
        print("Tebrikler! Doğru tahmin.")
        break
        