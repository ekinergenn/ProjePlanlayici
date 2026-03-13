import json
import os
import sys
from distutils.command.check import check
from tkinter.simpledialog import Dialog

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
                               QLabel, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget, QLineEdit, QTextEdit, QInputDialog, QMessageBox)

from backend.Proje import Proje


# DUZENLE KISMIDA AYNI OLACAK AMA PLACE HOLDERLARDA VAR OLANLAR YAZACAK
class ProjeEkle(object):
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

        #dosya konumu line edit
        self.dosyaLine = QLineEdit(Dialog)
        self.dosyaLine.setObjectName(u"dosyaLine")
        self.dosyaLine.setMaximumSize(QSize(180, 20))
        self.dosyaLine.setMinimumSize(QSize(180, 20))
        self.dosyaLine.setStyleSheet("background-color: #696969;"
                                    "color: white;"
                                    "border-radius: 5px;")
        self.dosyaLine.setCursor(Qt.CursorShape.PointingHandCursor)
        self.dosyaLine.setPlaceholderText("Dosya Konumu...")

        self.gridLayout.addWidget(self.dosyaLine, 5, 2, 1, 1)

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

        #buton baglantilari
        self.kaydetButon.clicked.connect(lambda: self.jsona_kaydet(Dialog))
        self.ekleButon.clicked.connect(self.yapilacakEklePopup)
        self.secilenButon.clicked.connect(self.secilenSil)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Proje Planlayıcı", u"Proje Planlayıcı", None))
        Dialog.setStyleSheet("background-color: #969696;")
        self.yapilacaklarLbl.setText(QCoreApplication.translate("Dialog", u"Yapılacaklar", None))
        self.gitLine.setText(QCoreApplication.translate("Dialog", None))
        self.geriButon.setText(QCoreApplication.translate("Dialog", u"Geri Dön", None))
        self.adLine.setText(QCoreApplication.translate("Dialog",None))
        self.kaydetButon.setText(QCoreApplication.translate("Dialog", u"Kaydet", None))
        self.dillerTxtEdit.setText(QCoreApplication.translate("Dialog", None))
        self.ekleButon.setText(QCoreApplication.translate("Dialog", u"Ekle", None))
        self.secilenButon.setText(QCoreApplication.translate("Dialog", u"Seçilenleri Sil", None))
        self.ilerlemeLbl.setText(QCoreApplication.translate("Dialog", u"İlerleme: %x", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 1", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 2", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Örnek Yapılacak 3", None))
        self.amacTxtEdit.setText(QCoreApplication.translate("Dialog", None))
    # retranslateUi

    def dosyaYoluBul(self, goreceli_yol):
        if getattr(sys, 'frozen', False):
            base_path = os.environ.get('RESOURCEPATH', os.path.join(os.path.dirname(sys.executable), '..', 'Resources'))
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, goreceli_yol)

    def jsona_kaydet(self, Dialog):
        yapilacakSayisi = 0
        yapilmislarSayisi = 0
        ilerlemeHesap = 0
        for i in range(self.verticalLayout.count()):
            w = self.verticalLayout.itemAt(i).widget()
            if isinstance(w, QCheckBox):
                yapilacakSayisi+=1
                if w.isChecked():
                    yapilmislarSayisi+=1

        if yapilacakSayisi > 0:
            ilerlemeHesap = (yapilmislarSayisi / float(yapilacakSayisi)) * 100
        else:
            ilerlemeHesap = 0.0

        yeni_proje = {
            "ad": self.adLine.text().strip(),
            "amac": self.amacTxtEdit.toPlainText().strip(),
            "ilerleme": ilerlemeHesap,
            "yapilacaklar": self.yapilacaklarAl(),
            "github": self.gitLine.text().strip(),
            "diller": [dil.strip() for dil in self.dillerTxtEdit.toPlainText().split(",") if dil.strip()],
            "dosya": self.dosyaLine.text().strip(),
        }

        dosya_yolu = self.dosyaYoluBul("data/projeler.json")

        try:
            with open(dosya_yolu, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"proje": []}
        if "proje" in data:
            data["proje"].append(yeni_proje)
        else:
            data["proje"] = [yeni_proje]

        try:
            with open(dosya_yolu, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Dosya yazılırken hata oluştu: {e}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Proje Ekleme")
        msg.setText("Proje başarıyla kaydedildi.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        Dialog.close()

    def yapilacaklarAl(self):
        liste = []
        # Layout içindeki her şeyi tek tek kontrol et
        for i in range(self.verticalLayout.count()):
            item = self.verticalLayout.itemAt(i)
            if item is None: continue

            widget = item.widget()
            # Sadece QCheckBox olanları ve boş olmayanları al
            if isinstance(widget, QCheckBox):
                metin = widget.text().strip()
                if metin:
                    liste.append({
                        "is": metin,
                        "durum": widget.isChecked()
                    })

        print(f"DEBUG: Fonksiyondan çıkan toplam eleman: {len(liste)}")
        return liste

    def yapilacakEklePopup(self):
        text, ok = QInputDialog.getText(None, 'Yeni Görev', 'Yapılacak işi giriniz:')

        if ok and text.strip():
            self.yeniCheckbox(text)

    def yeniCheckbox(self, gorev_metni):
        yeni_check = QCheckBox(self.scrollAreaWidgetContents)

        yeni_check.setText(gorev_metni)
        yeni_check.setStyleSheet("color: white; font-size: 14px;")

        self.verticalLayout.addWidget(yeni_check)

    def secilenSil(self):
        for i in reversed(range(self.verticalLayout.count())):
            item = self.verticalLayout.itemAt(i)
            widget = item.widget()

            if isinstance(widget, QCheckBox) and widget.isChecked():
                self.verticalLayout.removeWidget(widget)
                widget.deleteLater()

class ProjeEklePenceresi(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ProjeEkle()
        self.ui.setupUi(self)
        self.ui.geriButon.clicked.connect(self.close)