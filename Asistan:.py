class Asistan:
    def __init__(self, isim):
        self.isim = isim
        self.islem_sayisi = 0  

    def selam_ver(self, kullanici_adi):
        print(f"Merhaba {kullanici_adi}, ben {self.isim}. Sana nasıl yardım edebilirim?")
        self.islem_sayisi += 1  

    def durum_raporu(self):
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")


# Test
asistanim = Asistan("RoboBade")

asistanim.selam_ver("Bade")   # 1. işlem
asistanim.selam_ver("Bade")   # 2. işlem
asistanim.selam_ver("Ahmet")    # 3. işlem

asistanim.durum_raporu()      # Toplam 3 işlem