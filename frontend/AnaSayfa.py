import sys

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

        # ORNEKLER
        self.proje1 = ProjeWidget("Proje1",45)
        self.proje2 = ProjeWidget("Proje1", 45)
        self.proje3 = ProjeWidget("Proje1", 45)
        self.proje4 = ProjeWidget("Proje1", 45)
        self.scrollLayout.addWidget(self.proje1, 1)
        self.scrollLayout.addWidget(self.proje2, 1)
        self.scrollLayout.addWidget(self.proje3, 2)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)

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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Proje Planlayıcı", None))
        Dialog.setStyleSheet("background-color: #969696;")
        self.ekleButon.setText(QCoreApplication.translate("Dialog", u"Ekle", None))
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