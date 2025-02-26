import sys
from PyQt6.QtWidgets import QApplication
from Kelime_yonetimi import kelimeleri_yukle, kelime_ekle, kelime_sil, anlam_getir
from arama import kelime_ara
from ui import SozlukUI

def main():
    app = QApplication(sys.argv)
    sozluk = kelimeleri_yukle()  # ✅ Dosyadan kelimeleri yüklüyoruz

    def ekle_fonk(kelime,anlam):
        return kelime_ekle(kelime,anlam)

    def sil_fonk(kelime):
        return kelime_sil(kelime)

    def ara_fonk(harf):
        return kelime_ara(sozluk, harf)

    pencere = SozlukUI(ekle_fonk, sil_fonk, ara_fonk, anlam_getir, kelimeleri_yukle) 
    pencere.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

