import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QApplication, QDialog, \
    QStyleOption, QStyle
from PySide6.QtCore import Signal, Qt
from shiboken6.Shiboken import Object

from backend.Proje import Proje


class ProjeWidget(QWidget):
    ana_sayfayi_tazele_sinyali = Signal(Object)
    def __init__(self, proje : Proje):
        super().__init__()
        self.proje = proje

        if isinstance(proje, dict):
            ad = proje.get("ad")
            ilerleme = proje.get("ilerleme")
        else:
            ad = proje.ad
            ilerleme = proje.ilerleme

        self.projeAdi = QLabel(str(ad))

        self.setMaximumHeight(50)

        self.layout = QHBoxLayout(self)

        #proje adı
        self.projeAdi = QLabel(proje.ad)
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
        self.oran = QLabel(f"%{proje.ilerleme}")
        self.oran.setStyleSheet("background-color: transparent;"
                                "color: white;")
        self.oran.setMaximumSize(40, 20)

        self.layout.addWidget(self.projeAdi)
        self.layout.addWidget(self.goruntuleButonu)
        self.layout.addWidget(self.oran)

        self.setStyleSheet("ProjeWidget{"
                           "border: 2px solid black;"
                           "border-radius: 10px;}")

        self.goruntuleButonu.clicked.connect(self.goruntuleAc)

    def tiklanmaEvent(self, event):
        self.tiklandi.emit(self.proje)

    def goruntuleAc(self):
        from frontend.Goruntule import GoruntulePenceresi
        self.goruntulepencere = GoruntulePenceresi(self.proje)
        self.goruntulepencere.show()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)