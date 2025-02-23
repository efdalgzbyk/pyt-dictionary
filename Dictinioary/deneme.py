import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QTextEdit
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class DictionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Az-Dictionary")
        self.setGeometry(100, 100, 600, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("#exp. kelimenin girileceği yer")
        layout.addWidget(self.search_bar)
        
        # Word label
        self.word_label = QLabel("###WORD")
        layout.addWidget(self.word_label)
        
        # Word meanings
        self.meaning_fields = []
        for i in range(1, 6):
            line_edit = QLineEdit(f"Word meaning No.{i}")
            self.meaning_fields.append(line_edit)
            layout.addWidget(line_edit)
        
        central_widget.setLayout(layout)
        
        # Top Bar (Logo & Menu)
        self.menu_bar = self.menuBar()
        self.menu_bar.addMenu("☰")
        
        # Logo button (Placeholder)
        self.logo_button = QPushButton("Logo")
        self.logo_button.setEnabled(False)
        self.logo_button.setFixedSize(50, 25)
        self.menu_bar.setCornerWidget(self.logo_button, Qt.Corner.TopRightCorner)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec())
