"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""


class VeriAnaliziAraci:
    def __init__(self, veriler) -> None:
        self.veriler = veriler

    def toplamHesapla(self):
        toplam = sum(self.veriler)
        print(f"Toplam: {toplam}")

    def ortalamaHesapla(self):
        ortalama = sum(self.veriler) / len(self.veriler)
        print(f"Ortalama: {ortalama}")

    def gosterMax(self):
        maksimum = max(self.veriler)
        print(f"En büyük değer: {maksimum}")

    def gosterMin(self):
        minimum = min(self.veriler)
        print(f"En küçük değer: {minimum}")


analiz1 = VeriAnaliziAraci([10, 20, 30, 40, 50])

analiz1.toplamHesapla()
analiz1.ortalamaHesapla()
analiz1.gosterMax()
analiz1.gosterMin()

"""
Toplam: 150
Ortalama: 30.0
En büyük değer: 50
En küçük değer: 10
"""
