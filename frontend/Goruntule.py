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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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

        self.gridLayout.addWidget(self.gitButon, 2, 2, 1, 1, Qt.AlignCenter)

        #geri dön butonu
        self.geriButon = QPushButton(Dialog)
        self.geriButon.setObjectName(u"geriButon")
        self.geriButon.setMaximumSize(QSize(100, 20))
        self.geriButon.setMinimumSize(QSize(100, 20))
        self.geriButon.setStyleSheet("background-color: rgb(200, 20, 20);"
                                     "font: bold;"
                                     "border-radius: 10px;")
        self.geriButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.geriButon, 0, 0, 1, 1)

        #proje adı labelı
        self.adLbl = QLabel(Dialog)
        self.adLbl.setObjectName(u"adLbl")
        self.adLbl.setMaximumSize(QSize(150, 35))
        self.adLbl.setMinimumSize(QSize(150, 35))
        self.adLbl.setStyleSheet("color: black;"
                                 "font: 30px bold;")

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

        self.gridLayout.addWidget(self.duzenleButon, 0, 2, 1, 1, Qt.AlignCenter)

        #diller labelı
        self.dillerLbl = QLabel(Dialog)
        self.dillerLbl.setObjectName(u"dillerLbl")
        self.dillerLbl.setMaximumSize(QSize(1000, 1000))

        self.gridLayout.addWidget(self.dillerLbl, 3, 2, 1, 1, Qt.AlignCenter)

        self.ilerlemeLbl = QLabel(Dialog)
        self.ilerlemeLbl.setObjectName(u"ilerlemeLbl")

        self.gridLayout.addWidget(self.ilerlemeLbl, 4, 2, 1, 1, Qt.AlignCenter)

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

        #scroll areadaki check boxlar ornek
        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 1, 3, 1, Qt.AlignCenter)

        # proje amacının yazılı oldugu label
        self.amacLbl = QLabel(Dialog)
        self.amacLbl.setObjectName(u"amacLbl")

        self.gridLayout.addWidget(self.amacLbl, 1, 0, 4, 1, Qt.AlignCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        Dialog.setStyleSheet("background-color: #969696;")
        self.yapilacaklarLbl.setText(QCoreApplication.translate("Dialog", u"Yapılacaklar", None))
        self.gitButon.setText(QCoreApplication.translate("Dialog", u"Github Repostory", None))
        self.geriButon.setText(QCoreApplication.translate("Dialog", u"Geri Dön", None))
        self.adLbl.setText(QCoreApplication.translate("Dialog", u"Proje Adı", None))
        self.duzenleButon.setText(QCoreApplication.translate("Dialog", u"Düzenle", None))
        self.dillerLbl.setText(QCoreApplication.translate("Dialog", u"Kullanılan Diller: (python vs alt alt yazılacak)", None))
        self.ilerlemeLbl.setText(QCoreApplication.translate("Dialog", u"İlerleme: %x", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 1", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 2", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 3", None))
        self.amacLbl.setText(QCoreApplication.translate("Dialog", u"Amaç: Proje Amacı Buraya Yazılacak", None))
    # retranslateUi

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