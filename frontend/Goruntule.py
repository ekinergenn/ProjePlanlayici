import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

from backend.Proje import Proje


class Ui_Dialog(object):
    def setupUi(self, Dialog, proje : Proje):

        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(844, 612)
        
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")

        #yapılacaklar labelı
        self.yapilacaklarLbl = QLabel(Dialog)
        self.yapilacaklarLbl.setObjectName(u"yapilacaklarLbl")
        self.yapilacaklarLbl.setMaximumSize(QSize(150, 20))
        self.yapilacaklarLbl.setMinimumSize(QSize(150, 20))
        self.yapilacaklarLbl.setStyleSheet("font: bold;")
        self.yapilacaklarLbl.setText("Yapılacaklar")

        self.gridLayout.addWidget(self.yapilacaklarLbl, 1, 1, 1, 1)

        #github repo suna yonlendiren buton
        self.gitButon = QPushButton(Dialog)
        self.gitButon.setObjectName(u"gitButon")
        self.gitButon.setMaximumSize(QSize(180, 20))
        self.gitButon.setMinimumSize(QSize(180, 20))
        self.gitButon.setStyleSheet("background-color: black;"
                                     "color: white;"
                                     "font-weight: bold;"
                                     "border-radius: 10px;")
        self.gitButon.setCursor(Qt.CursorShape.PointingHandCursor)
        self.gitButon.setText("GitHub Repository")

        self.gridLayout.addWidget(self.gitButon, 2, 2, 1, 1, Qt.AlignCenter)

        #dosya konumu butonu
        self.dosyaButon = QPushButton(Dialog)
        self.dosyaButon.setObjectName(u"dosyaButon")
        self.dosyaButon.setMaximumSize(QSize(160, 20))
        self.dosyaButon.setMinimumSize(QSize(160, 20))
        self.dosyaButon.setStyleSheet("background-color: black;"
                                     "color: white;"
                                     "font-weight: bold;"
                                     "border-radius: 10px;")
        self.dosyaButon.setCursor(Qt.CursorShape.PointingHandCursor)
        self.dosyaButon.setText("Dosya Konumu")

        self.gridLayout.addWidget(self.dosyaButon, 5, 2, 1, 1)

        #geri dön butonu
        self.geriButon = QPushButton(Dialog)
        self.geriButon.setObjectName(u"geriButon")
        self.geriButon.setMaximumSize(QSize(100, 20))
        self.geriButon.setMinimumSize(QSize(100, 20))
        self.geriButon.setStyleSheet("background-color: rgb(200, 20, 20);"
                                     "font: bold;"
                                     "border-radius: 10px;")
        self.geriButon.setCursor(Qt.CursorShape.PointingHandCursor)
        self.geriButon.setText("Geri Dön")

        self.gridLayout.addWidget(self.geriButon, 0, 0, 1, 1)

        #proje adı labelı
        self.adLbl = QLabel(Dialog)
        self.adLbl.setObjectName(u"adLbl")
        self.adLbl.setMaximumSize(QSize(150, 35))
        self.adLbl.setMinimumSize(QSize(150, 35))
        self.adLbl.setStyleSheet("color: black;"
                                 "font: 30px bold;")
        self.adLbl.setText(proje.ad)

        self.gridLayout.addWidget(self.adLbl, 0, 1, 1, 1, Qt.AlignCenter)

        #duzenle butonu
        self.duzenleButon = QPushButton(Dialog)
        self.duzenleButon.setObjectName(u"duzenleButon")
        self.duzenleButon.setMaximumSize(QSize(100, 20))
        self.duzenleButon.setMinimumSize(QSize(100, 20))
        self.duzenleButon.setStyleSheet("background-color: black;"
                                     "color: white;"
                                     "font-weight: bold;"
                                     "border-radius: 10px;")
        self.duzenleButon.setCursor(Qt.CursorShape.PointingHandCursor)
        self.duzenleButon.setText("Düzenle")

        self.gridLayout.addWidget(self.duzenleButon, 0, 2, 1, 1, Qt.AlignCenter)

        #diller labelı
        self.dillerLbl = QLabel(Dialog)
        self.dillerLbl.setObjectName(u"dillerLbl")
        self.dillerLbl.setMaximumSize(QSize(1000, 1000))
        diller_metni = ", ".join(proje.diller)
        self.dillerLbl.setText(f"Kullanılan Diller: {diller_metni}")

        self.gridLayout.addWidget(self.dillerLbl, 3, 2, 1, 1, Qt.AlignCenter)

        #ilerleme Label
        self.ilerlemeLbl = QLabel(Dialog)
        self.ilerlemeLbl.setObjectName(u"ilerlemeLbl")
        self.ilerlemeLbl.setText(f"%{proje.ilerleme}")

        self.gridLayout.addWidget(self.ilerlemeLbl, 4, 2, 1, 1, Qt.AlignCenter)

        #Scroll area (YAPILACAKLAR)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet("background-color: #3B3B3B;"
                                      "border: 1px #3B3B3B;"
                                      "border-radius: 10px;")
        self.scrollArea.setMinimumSize(QSize(500, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 518))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 1, 4, 1, Qt.AlignCenter)

        # proje amacının yazılı oldugu label
        self.amacLbl = QLabel(Dialog)
        self.amacLbl.setObjectName(u"amacLbl")
        self.amacLbl.setText(f"Amaç: {proje.amac}")

        self.gridLayout.addWidget(self.amacLbl, 1, 0, 5, 1, Qt.AlignCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Proje Planlayıcı", u"Proje Planlayıcı", None))
        Dialog.setStyleSheet("background-color: #969696;")
    # retranslateUi

class GoruntulePenceresi(QDialog):
    def __init__(self, proje:Proje):
        super().__init__()
        self.proje = proje
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, proje)
        self.ui.geriButon.clicked.connect(self.close)

        self.ui.adLbl.setText(self.proje.ad)
        diller_metni = ", ".join(self.proje.diller)
        self.ui.dillerLbl.setText(f"Kullanılan Diller: {diller_metni}")
        self.ui.ilerlemeLbl.setText(f"%{self.proje.ilerleme}")
        for yapilacak in self.proje.yapilacaklar:
            check = QCheckBox(self.ui.scrollAreaWidgetContents)
            check.setText(f"{yapilacak}")
            check.setStyleSheet("color: white;")
            self.ui.verticalLayout.addWidget(check)
        self.ui.amacLbl.setText(proje.amac)