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
                               QVBoxLayout, QWidget, QLineEdit, QTextEdit)

# DUZENLE KISMIDA AYNI OLACAK AMA PLACE HOLDERLARDA VAR OLANLAR YAZACAK
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(844, 612)

        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")

        # yapılacaklar labelı
        self.yapilacaklarLbl = QLabel(Dialog)
        self.yapilacaklarLbl.setObjectName(u"yapilacaklarLbl")
        self.yapilacaklarLbl.setMaximumSize(QSize(150, 20))
        self.yapilacaklarLbl.setMinimumSize(QSize(150, 20))
        self.yapilacaklarLbl.setStyleSheet("font: bold;")

        self.gridLayout.addWidget(self.yapilacaklarLbl, 1, 1, 1, 1)

        # github repo sunu alan lineedit
        self.gitLine = QLineEdit(Dialog)
        self.gitLine.setObjectName(u"gitLine")
        self.gitLine.setMaximumSize(QSize(180, 20))
        self.gitLine.setMinimumSize(QSize(180, 20))
        self.gitLine.setStyleSheet("background-color: #696969;"
                                    "color: white;"
                                    "border-radius: 5px;")
        self.gitLine.setPlaceholderText("GitHub Repostory Linki...")
        self.gitLine.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.gitLine, 2, 2, 1, 2, Qt.AlignCenter)

        # geri dön butonu
        self.geriButon = QPushButton(Dialog)
        self.geriButon.setObjectName(u"geriButon")
        self.geriButon.setMaximumSize(QSize(100, 20))
        self.geriButon.setMinimumSize(QSize(100, 20))
        self.geriButon.setStyleSheet("background-color: rgb(200, 20, 20);"
                                     "font: bold;"
                                     "border-radius: 10px;")
        self.geriButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.geriButon, 0, 0, 1, 1)

        # proje adı lineedit
        self.adLine = QLineEdit(Dialog)
        self.adLine.setObjectName(u"adLine")
        self.adLine.setMaximumSize(QSize(150, 35))
        self.adLine.setMinimumSize(QSize(150, 35))
        self.adLine.setStyleSheet("color: black;"
                                 "font: 30px bold;")
        self.adLine.setPlaceholderText("Proje Adı...")
        self.adLine.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.adLine, 0, 1, 1, 1, Qt.AlignCenter)

        # kaydet butonu
        self.kaydetButon = QPushButton(Dialog)
        self.kaydetButon.setObjectName(u"kaydetButon")
        self.kaydetButon.setMaximumSize(QSize(100, 20))
        self.kaydetButon.setMinimumSize(QSize(100, 20))
        self.kaydetButon.setStyleSheet("background-color: black;"
                                        "color: white;"
                                        "font-weight: bold;"
                                        "border-radius: 10px;")
        self.kaydetButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.kaydetButon, 0, 2, 1, 1, Qt.AlignCenter)

        # sil butonu
        self.silButon = QPushButton(Dialog)
        self.silButon.setObjectName(u"silButon")
        self.silButon.setMaximumSize(QSize(70, 20))
        self.silButon.setMinimumSize(QSize(70, 20))
        self.silButon.setStyleSheet("background-color: rgb(200, 0, 0);"
                                    "color: white;"
                                     "font: bold;"
                                     "border-radius: 10px;")
        self.silButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.silButon, 0, 3, 1, 1)

        # ekle butonu
        self.ekleButon = QPushButton(Dialog)
        self.ekleButon.setObjectName(u"ekleButon")
        self.ekleButon.setMaximumSize(QSize(70, 20))
        self.ekleButon.setMinimumSize(QSize(70, 20))
        self.ekleButon.setStyleSheet("background-color: black;"
                                        "color: white;"
                                        "font-weight: bold;"
                                        "border-radius: 10px;")
        self.ekleButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.ekleButon, 5, 1, 1, 1)

        # altındaki secilenleri sil butonu
        self.secilenButon = QPushButton(Dialog)
        self.secilenButon.setObjectName(u"secilenButon")
        self.secilenButon.setMaximumSize(QSize(150, 20))
        self.secilenButon.setMinimumSize(QSize(150, 20))
        self.secilenButon.setStyleSheet("background-color: red;"
                                        "color: white;"
                                        "font-weight: bold;"
                                        "border-radius: 10px;")
        self.secilenButon.setCursor(Qt.CursorShape.PointingHandCursor)

        self.gridLayout.addWidget(self.secilenButon, 6, 1, 1, 1)

        # diller textedit
        self.dillerTxtEdit = QTextEdit(Dialog)
        self.dillerTxtEdit.setObjectName(u"dillerTxtEdit")
        self.dillerTxtEdit.setMaximumSize(QSize(1000, 1000))
        self.dillerTxtEdit.setPlaceholderText("Kullanılan Dilleri Giriniz:")

        self.gridLayout.addWidget(self.dillerTxtEdit, 3, 2, 1, 2, Qt.AlignCenter)

        #ilerleme lbl değiştirilemez mevcut yapılacaklar sayısı ile tamamlanmış yapılanlar oranıdır
        self.ilerlemeLbl = QLabel(Dialog)
        self.ilerlemeLbl.setObjectName(u"ilerlemeLbl")

        self.gridLayout.addWidget(self.ilerlemeLbl, 4, 2, 1, 2, Qt.AlignCenter)

        #scroll areada bir farklılık yok
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

        # scroll areadaki check boxlar ornek
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

        # proje amacı textedit
        self.amacTxtEdit = QTextEdit(Dialog)
        self.amacTxtEdit.setObjectName(u"amacTxtEdit")
        self.amacTxtEdit.setPlaceholderText("Projenin amacını giriniz...")
        self.amacTxtEdit.setMinimumSize(300,300)

        self.gridLayout.addWidget(self.amacTxtEdit, 1, 0, 4, 1, Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        Dialog.setStyleSheet("background-color: #969696;")
        self.yapilacaklarLbl.setText(QCoreApplication.translate("Dialog", u"Yapılacaklar", None))
        self.gitLine.setText(QCoreApplication.translate("Dialog", None))
        self.geriButon.setText(QCoreApplication.translate("Dialog", u"Geri Dön", None))
        self.adLine.setText(QCoreApplication.translate("Dialog",None))
        self.kaydetButon.setText(QCoreApplication.translate("Dialog", u"Düzenle", None))
        self.silButon.setText(QCoreApplication.translate("Dialog", u"Sil", None))
        self.dillerTxtEdit.setText(QCoreApplication.translate("Dialog", None))
        self.ekleButon.setText(QCoreApplication.translate("Dialog", u"Ekle", None))
        self.secilenButon.setText(QCoreApplication.translate("Dialog", u"Seçilenleri Sil", None))
        self.ilerlemeLbl.setText(QCoreApplication.translate("Dialog", u"İlerleme: %x", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 1", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 2", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 3", None))
        self.amacTxtEdit.setText(QCoreApplication.translate("Dialog", None))
    # retranslateUi


# main       --DAHA SONRA SİLİNECEK--
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