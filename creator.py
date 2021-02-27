from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import json

with open('horario.json') as json_file: 
    data = json.load(json_file) 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Diario de Bordo Creator")
        MainWindow.resize(264, 196)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.diaDaSemana = QtWidgets.QTextEdit(self.centralwidget)
        self.diaDaSemana.setGeometry(QtCore.QRect(110, 0, 141, 31))
        self.diaDaSemana.setObjectName("diaDaSemana")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 101, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.cadeira = QtWidgets.QTextEdit(self.centralwidget)
        self.cadeira.setGeometry(QtCore.QRect(110, 30, 141, 31))
        self.cadeira.setAutoFillBackground(True)
        self.cadeira.setMarkdown("")
        self.cadeira.setObjectName("cadeira")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 101, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.hI = QtWidgets.QTextEdit(self.centralwidget)
        self.hI.setGeometry(QtCore.QRect(110, 60, 141, 31))
        self.hI.setObjectName("hI")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 101, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.hF = QtWidgets.QTextEdit(self.centralwidget)
        self.hF.setGeometry(QtCore.QRect(110, 90, 141, 31))
        self.hF.setObjectName("hF")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(0, 123, 251, 41))
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.submit.clicked.connect(self.adiciona)
    def adiciona(self):
        dia = self.diaDaSemana.toPlainText().lower()
        cadeira = (self.cadeira.toPlainText()).upper()
        hi = (self.hI.toPlainText()).lower()
        hf = (self.hF.toPlainText()).lower()
        # so tem um: =len(hi.split(':'))==2==len(hf.split(':'))
        hi1,hi2=hi.split(':')
        hf1,hf2=hf.split(':')
        # digit = hi1.isdigit() and hi2.isdigit() and hf1.isdigit() and hf2.isdigit()
        # validos = 0<=int(hi1)<24 and 0<=int(hf1)<24 and 0<=int(hi2)<60 and 0<=int(hf2)<60
        if (not (dia=="" or cadeira=="" or hi=="" or hf=="")) and len(hi.split(':'))==2==len(hf.split(':')) and hi1.isdigit() and hi2.isdigit() and hf1.isdigit() and hf2.isdigit() and 0<=int(hi1)<24 and 0<=int(hf1)<24 and 0<=int(hi2)<60 and 0<=int(hf2)<60:
            assert()
            if not dia in data:
                data[dia] = { cadeira : [{ "hora inicial" : hi,"hora final" :hf}] }
            else:
                dia=data[dia]
                if not cadeira in dia:
                    dia[cadeira] =  [{ "hora inicial" : hi,"hora final" :hf}]
                else:
                    dia[cadeira].append({ "hora inicial" : hi,"hora final" :hf})
            json_object = json.dumps(data, indent = 4)
            with open("horario.json", "w") as outfile: 
                outfile.write(json_object) 
            msg = QMessageBox()
            msg.setWindowTitle("Sucesso")
            msg.setText("AULA ADICIONADA COM SUCESSO!!!!!")
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("por favor escreve coisas")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

                




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.diaDaSemana.setPlaceholderText(_translate("MainWindow", "segunda"))
        self.label.setText(_translate("MainWindow", "dia da semana"))
        self.label_2.setText(_translate("MainWindow", "cadeira"))
        self.cadeira.setPlaceholderText(_translate("MainWindow", "Matematica"))
        self.label_3.setText(_translate("MainWindow", "hora de inicio"))
        self.hI.setPlaceholderText(_translate("MainWindow", "8:00"))
        self.label_4.setText(_translate("MainWindow", "hora de fim"))
        self.hF.setPlaceholderText(_translate("MainWindow", "16:00"))
        self.submit.setText(_translate("MainWindow", "submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())