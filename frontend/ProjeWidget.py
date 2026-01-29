import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QApplication, QDialog


class ProjeWidget(QWidget):
    def __init__(self, proje_adi, tamamlama_orani):
        super().__init__()

        self.setMaximumHeight(50)

        self.layout = QHBoxLayout(self)

        #proje adı
        self.projeAdi = QLabel(proje_adi)
        self.projeAdi.setStyleSheet("background-color: transparent;"
                                     "color: white;")

        #goruntule butonu
        self.goruntuleButonu = QPushButton("Görüntüle")
        self.goruntuleButonu.setStyleSheet("color: white;"
                                           "background-color: gray;"
                                           "border: 1px solid black;"
                                           "border-radius: 5px;")
        self.goruntuleButonu.setMaximumSize(100, 20)
        self.goruntuleButonu.setMinimumSize(100, 20)
        self.goruntuleButonu.setCursor(Qt.CursorShape.PointingHandCursor)

        #tamamlanma oranı kısmı
        self.oran = QLabel(f"%{tamamlama_orani}")
        self.oran.setStyleSheet("background-color: transparent;"
                                "color: white;")
        self.oran.setMaximumSize(30, 20)

        self.layout.addWidget(self.projeAdi)
        self.layout.addWidget(self.goruntuleButonu)
        self.layout.addWidget(self.oran)

        self.setStyleSheet("background-color: #f0f0f0; border-radius: 5px;")