class calisan:
    def __init__(self,ad,soyad,yas) -> None:
        self.get_ad=ad
        self.get_soyad=soyad
        self.get_yas=yas

personel1=calisan("Sena","Bitirgen",21)

print(personel1.get_ad)