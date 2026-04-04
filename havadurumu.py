import random

class HavaDurumu:
    def __init__(self):
        self.durum = "Güneşli"  # başlangıç durumu

    def yarin_ne_olacak(self):
        rastgele_sayi = random.random()  # 0 ile 1 arasında sayı

        if self.durum == "Güneşli":
            if rastgele_sayi < 0.8:
                self.durum = "Güneşli"
            else:
                self.durum = "Yağmurlu"

        elif self.durum == "Yağmurlu":
            if rastgele_sayi < 0.7:
                self.durum = "Yağmurlu"
            else:
                self.durum = "Güneşli"

        return self.durum


# nesne oluşturma
hava = HavaDurumu()

# ilk günü yazdır
print(f"1. Gün: {hava.durum}")

# 10 günlük simülasyon
for gun in range(2, 11):
    sonuc = hava.yarin_ne_olacak()
    print(f"{gun}. Gün: {sonuc}")