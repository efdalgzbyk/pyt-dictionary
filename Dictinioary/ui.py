from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QMainWindow
from Kelime_yonetimi import kelimeleri_yukle

class SozlukUI(QMainWindow):
    def __init__(self, ekle_fonk, sil_fonk, ara_fonk):
        super().__init__()
        self.ekle_fonk = ekle_fonk
        self.sil_fonk = sil_fonk
        self.ara_fonk = ara_fonk
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sözlük Uygulaması")
        self.setGeometry(100, 100, 400, 300)

        merkezi_widget = QWidget()
        self.setCentralWidget(merkezi_widget)

        layout = QVBoxLayout()

        self.kelimeInput = QLineEdit(self)
        self.kelimeInput.setPlaceholderText("Kelime gir...")
        layout.addWidget(self.kelimeInput)

        self.ekleButon = QPushButton("Kelime Ekle", self)
        self.ekleButon.clicked.connect(self.kelimeEkle)
        layout.addWidget(self.ekleButon)

        self.silButon = QPushButton("Seçili Kelimeyi Sil", self)
        self.silButon.clicked.connect(self.kelimeSil)
        layout.addWidget(self.silButon)

        self.aramaInput = QLineEdit(self)
        self.aramaInput.setPlaceholderText("Harfe göre ara...")
        self.aramaInput.textChanged.connect(self.kelimeAra)
        layout.addWidget(self.aramaInput)

        self.kelimeListesi = QListWidget(self)
        layout.addWidget(self.kelimeListesi)

        merkezi_widget.setLayout(layout)

        # 🌟 Uygulama açıldığında kayıtlı kelimeleri yükle
        self.kelimeleri_listele()

    def kelimeEkle(self):
        kelime = self.kelimeInput.text().strip()
        if kelime:
            if self.ekle_fonk(kelime):
                self.kelimeListesi.addItem(kelime)
            self.kelimeInput.clear()

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

    def kelimeleri_listele(self):
        """Mevcut kelimeleri listeye ekler."""
        self.kelimeListesi.clear()  # Önce listeyi temizle
        sozluk = kelimeleri_yukle()  # Dosyadan kelimeleri al
        self.kelimeListesi.addItems(sorted(sozluk))  # Kelimeleri ekle
