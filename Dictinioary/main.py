import sys
from PyQt6.QtWidgets import QApplication
from Kelime_yonetimi import kelimeleri_yukle, kelime_ekle, kelime_sil
from arama import kelime_ara
from ui import SozlukUI

def main():
    app = QApplication(sys.argv)
    sozluk = kelimeleri_yukle()  # Artık bir set

    def ekle_fonk(kelime):
        return kelime_ekle(sozluk, kelime)

    def sil_fonk(kelime):
        return kelime_sil(sozluk, kelime)

    def ara_fonk(harf):
        return kelime_ara(sozluk, harf)

    pencere = SozlukUI(ekle_fonk, sil_fonk, ara_fonk)
    pencere.show()
    pencere.kelimeleri_listele() 
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
