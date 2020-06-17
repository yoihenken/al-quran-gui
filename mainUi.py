import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from detail_dialog import *
import requests

baseUrl = 'https://api.quran.sutanlab.id/surah/'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.surat = QtWidgets.QLabel('Surat-surat Al-\'quran')
        self.daftarSurat = QtWidgets.QListWidget()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 584, 332))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.daftarSurat)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2,)
        self.verticalLayout.addWidget(self.surat)
        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.daftarSurat.doubleClicked.connect(self.suratDetail)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Al-Qur\'an"))
        
    def fetchSurat(self):
        self.getAllSurat = requests.get(baseUrl).json()
        data = self.getAllSurat['data']
        self.listSurat(data)

    def listSurat(self,data=[]):
        for item in data:
            self.daftarSurat.addItem(item['englishName'])
    
    def suratDetail(self):
        Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.getDetailSurat = requests.get(baseUrl+str(self.daftarSurat.currentRow()+1)).json()
        data = self.getDetailSurat['data']
        self.ui.setupUi(Dialog) 
        self.ui.getSurat(data)
        Dialog.show()
        Dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.fetchSurat()
    MainWindow.show()
    sys.exit(app.exec_())
