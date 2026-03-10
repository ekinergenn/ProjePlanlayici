import json
import sys
from tokenize import String

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QWidget, QLineEdit, QVBoxLayout)

from ProjeWidget import ProjeWidget
from backend.Proje import Proje
from ProjeEkle import ProjeEklePenceresi


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(727, 493)

        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)

        # Scroll Area
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 701, 427))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet(u"background-color: transparent;")
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.scrollLayout.setAlignment(Qt.AlignTop)
        self.scrollLayout.setSpacing(5)

        # proje widgetları
        self.projeler = self.jsonVerileri()

        for i in range(len(self.projeler)):
            proje = Proje.from_dict(self.projeler[i])
            self.pWidget = ProjeWidget(proje)
            self.scrollLayout.addWidget(self.pWidget, 1)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 5)

        # Combo Box
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(170, 16777215))
        self.comboBox.setMinimumSize(QSize(170, 20))
        self.comboBox.addItems(["Tamamlanmış", "Tamamlanmamış"])
        self.comboBox.setStyleSheet("background-color: black;"
                                    "color: white;"
                                    "font: bold;"
                                    "border: 1px solid black;"
                                    "border-radius: 10px;"
                                    "padding: 5px;")
        self.comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        # Arama Alanı
        self.aramaCubugu = QLineEdit(Dialog)
        self.aramaCubugu.setObjectName(u"aramaCubugu")
        self.aramaCubugu.setMaximumSize(QSize(200, 16777215))
        self.aramaCubugu.setMinimumSize(QSize(50, 20))
        self.aramaCubugu.setPlaceholderText("Ara...")
        self.aramaCubugu.setStyleSheet("background-color: gray;"
                                       "color: white;"
                                       "border: 1px solid black;"
                                       "border-radius: 7px;")
        self.aramaCubugu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.aramaCubugu, 0, 1, 1, 1)

        #Butonlar için sizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        # Arama Butonu
        self.aramaButonu = QPushButton(Dialog)
        self.aramaButonu.setObjectName(u"aramaButonu")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aramaButonu.sizePolicy().hasHeightForWidth())
        self.aramaButonu.setSizePolicy(sizePolicy)
        self.aramaButonu.setMinimumSize(QSize(100, 10))
        self.aramaButonu.setMaximumSize(QSize(100, 20))
        self.aramaButonu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.aramaButonu.setText("Ara")
        self.aramaButonu.setStyleSheet("background-color: gray;"
                                       "color: black;"
                                       "font: bold;"
                                       "border-radius: 7px;")
        self.gridLayout.addWidget(self.aramaButonu, 0, 2, 1, 1)

        # Ekle Butonu
        self.ekleButon = QPushButton(Dialog)
        self.ekleButon.setObjectName(u"ekleButon")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ekleButon.sizePolicy().hasHeightForWidth())
        self.ekleButon.setSizePolicy(sizePolicy)
        self.ekleButon.setMinimumSize(100, 20)
        self.ekleButon.setMaximumSize(QSize(100, 16777215))
        self.ekleButon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ekleButon.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ekleButon.setStyleSheet("background-color: black;"
                                     "color: white;"
                                     "font-weight: bold;"
                                     "border-radius: 10px;")

        self.gridLayout.addWidget(self.ekleButon, 0, 3, 1, 1)

        #yenile butonu
        self.yenileButon = QPushButton(Dialog)
        self.yenileButon.setObjectName(u"yenileButon")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yenileButon.sizePolicy().hasHeightForWidth())
        self.yenileButon.setSizePolicy(sizePolicy)
        self.yenileButon.setMinimumSize(100, 20)
        self.yenileButon.setMaximumSize(QSize(100, 16777215))
        self.yenileButon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.yenileButon.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.yenileButon.setStyleSheet("background-color: black;"
                                     "color: white;"
                                     "font-weight: bold;"
                                     "border-radius: 10px;")
        self.gridLayout.addWidget(self.yenileButon, 0, 4, 1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        #buton tıklamaları
        self.aramaButonu.clicked.connect(lambda: self.arama(self.projeler))
        self.comboBox.currentTextChanged.connect(lambda: self.tamamlanma(self.projeler, self.comboBox.currentText()))
        self.ekleButon.clicked.connect(lambda: self.ekleAc())
        self.yenileButon.clicked.connect(lambda: self.listeyi_tazele())

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Proje Planlayıcı", None))
        Dialog.setStyleSheet("background-color: #969696;")
        self.ekleButon.setText(QCoreApplication.translate("Dialog", u"Ekle", None))
        self.yenileButon.setText(QCoreApplication.translate("Dialog", u"Yenile", None))
    # retranslateUi

    def jsonVerileri(self):
        with open("../data/projeler.json", "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)
            return veri.get("proje", [])

    def arama(self, projeler):
        aranacak = self.aramaCubugu.text()
        uyumlu = []
        for veri in projeler:
            proje = Proje.from_dict(veri)
            if aranacak.lower() in proje.ad.lower():
                uyumlu.append(proje)
        self.sAreaGuncelle(uyumlu)

    def tamamlanma(self, projeler, tamamlama):
        uyumlu = []
        if tamamlama == "Tamamlanmış":
            for veri in projeler:
                proje = Proje.from_dict(veri)
                if proje.ilerleme == 100:
                    uyumlu.append(proje)
        else:
            for veri in projeler:
                proje = Proje.from_dict(veri)
                if proje.ilerleme != 100:
                    uyumlu.append(proje)

        self.sAreaGuncelle(uyumlu)

    def ekleAc(self):
        self.yeni_pencere = ProjeEklePenceresi()
        self.yeni_pencere.finished.connect(lambda: self.listeyi_tazele())
        self.yeni_pencere.show()

    def listeyi_tazele(self):
        self.projeler = []
        self.projeler = self.jsonVerileri()
        self.sAreaGuncelle(self.projeler)

    def sAreaGuncelle(self, liste):

        while self.scrollLayout.count():
            item = self.scrollLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for veri in liste:
            if isinstance(veri, dict):
                proje_objesi = Proje.from_dict(veri)
            else:
                proje_objesi = veri

            self.pWidget = ProjeWidget(proje_objesi)
            self.scrollLayout.addWidget(self.pWidget)

        self.scrollAreaWidgetContents.adjustSize()
        self.scrollArea.update()

#main       --DAHA SONRA SİLİNECEK--
class MyApp(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pencere = MyApp()
    pencere.show()

    sys.exit(app.exec())