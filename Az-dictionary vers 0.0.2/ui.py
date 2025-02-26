from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel, QMainWindow
from PyQt6.QtGui import QIcon
import os

class SozlukUI(QMainWindow):
    def __init__(self, ekle_fonk, sil_fonk, ara_fonk, anlam_fonk, kelimeleri_yukle):
        super().__init__()
        self.ekle_fonk = ekle_fonk
        self.sil_fonk = sil_fonk
        self.ara_fonk = ara_fonk
        self.anlam_fonk = anlam_fonk
        self.kelimeleri_yukle = kelimeleri_yukle  # Kelimeleri dosyadan yükleme fonksiyonu
        self.initUI()

    def get_icon_path(self, icon_name):
        return os.path.join(os.path.dirname(__file__), "Icon", icon_name)

    def initUI(self):
        self.setWindowTitle("Az-Dictionary")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon(self.get_icon_path("Icon.png")))  # 📌 Pencere ikonu

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        self.kelimeInput = QLineEdit(self)
        self.kelimeInput.setPlaceholderText("Kelime gir...")
        self.mainLayout.addWidget(self.kelimeInput)

        self.anlamInput= QLineEdit(self)
        self.anlamInput.setPlaceholderText("Anlamını giriniz")
        self.mainLayout.addWidget(self.anlamInput)

        self.ekleButon = QPushButton("Kelime Ekle", self)
        self.ekleButon.clicked.connect(self.kelimeEkle)
        self.mainLayout.addWidget(self.ekleButon)

        self.silButon = QPushButton("Seçili Kelimeyi Sil", self)
        self.silButon.clicked.connect(self.kelimeSil)
        self.mainLayout.addWidget(self.silButon)

        self.aramaInput = QLineEdit(self)
        self.aramaInput.setPlaceholderText("Harfe göre ara...")
        self.aramaInput.textChanged.connect(self.kelimeAra)
        self.mainLayout.addWidget(self.aramaInput)

        self.kelimeListesi = QListWidget(self)
        self.kelimeListesi.itemClicked.connect(self.kelimeSecildi)  
        self.mainLayout.addWidget(self.kelimeListesi)

        self.kelimeleri_listele()  # Başlangıçta kayıtlı kelimeleri listele

    def kelimeEkle(self):
        kelime = self.kelimeInput.text().strip()
        anlam = self.anlamInput.text().strip()
        
        if kelime and anlam:  # Hem kelime hem de anlam girilmiş mi?
            if self.ekle_fonk(kelime, anlam):  # Kelime ve anlamı ekle
                self.kelimeListesi.addItem(kelime)  # Sadece kelimeyi listeye ekle
            self.kelimeInput.clear()
            self.anlamInput.clear()

    def kelimeSil(self):
        secili_kelime = self.kelimeListesi.currentItem()
        if secili_kelime:
            kelime = secili_kelime.text()
            if self.sil_fonk(kelime):
                self.kelimeListesi.takeItem(self.kelimeListesi.row(secili_kelime))

    def kelimeAra(self):
        harf = self.aramaInput.text().strip().lower()
        self.kelimeListesi.clear()
        bulunanlar = self.ara_fonk(harf)
        self.kelimeListesi.addItems(bulunanlar)

    def kelimeSecildi(self, item):
        """Kelimeye tıklandığında anlam penceresini açar."""
        kelime = item.text()
        anlam = self.anlam_fonk(kelime)

        self.anlamPenceresi = AnlamPenceresi(self, kelime, anlam)
        self.anlamPenceresi.show()
        self.hide()  # Ana pencereyi gizle

    def kelimeleri_listele(self):
        """Dosyadan kayıtlı kelimeleri yükleyip listeye ekler."""
        self.kelimeListesi.clear()
        kelimeler = self.kelimeleri_yukle()  # Kayıtlı kelimeleri yükle
        self.kelimeListesi.addItems(sorted(kelimeler))

class AnlamPenceresi(QWidget):
    

    def __init__(self, ana_pencere, kelime, anlam):
        super().__init__()
        self.ana_pencere = ana_pencere
        self.setWindowTitle("Kelime Detayı")
        self.setGeometry(150, 150, 400, 200)
        self.setWindowIcon(QIcon(self.ana_pencere.get_icon_path("Icon.png")))  # 📌 Pencere ikonu
        layout = QVBoxLayout()

        self.kelimeLabel = QLabel(f"<b>Kelime:</b> {kelime}", self)
        layout.addWidget(self.kelimeLabel)

        self.anlamLabel = QLabel(f"<b>Anlam:</b> {anlam}", self)
        layout.addWidget(self.anlamLabel)

        self.geriButon = QPushButton("Geri Dön", self)
        self.geriButon.clicked.connect(self.geriDon)
        layout.addWidget(self.geriButon)

        self.setLayout(layout)

    def geriDon(self):
        """Geri dön butonuna basınca ana pencereyi geri getirir."""
        self.ana_pencere.show()
        self.close()
