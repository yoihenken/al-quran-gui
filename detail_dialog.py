
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 446)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 591, 381))
        self.listWidget.setObjectName("listWidget")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.closeFun)
        


    def closeFun(self):
        print('close')
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",'Nama Surat'))
        self.label_2.setText(_translate("Dialog", "Arti Indonesia"))
        self.pushButton.setText(_translate("Dialog", "Close"))

    def getSurat(self,data):
        
        suratList = data['ayahs']
        print(data['englishName'])
        englishName = str(data['englishName'])
        self.label.setText(englishName) ##yg ini gk bisa di set
        
        for item in suratList:
            self.listWidget.addItem(item['text']['arab']) ##sama ini
            print('%d\n', item['text']['arab'])
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    ui.close()
    self.close()
