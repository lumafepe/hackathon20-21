from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import pickle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(223, 192)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setGeometry(QtCore.QRect(30, 70, 160, 20))
        self.Slider.setMaximum(1)
        self.Slider.setPageStep(1)
        self.Slider.setProperty("value", 0)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 58, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 58, 18))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 223, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Slider.valueChanged.connect(self.faz)
    
    def faz(self):
        if (self.Slider.value()==0):
            pid = pickle.load( open( "pid", "rb" ) )
            os.system(f"kill -9 {pid}")
        
        else:
            subprocess.call("python main2.py &", shell=True)

    def closeEvent(self, event):
        pid = pickle.load( open( "pid", "rb" ) )
        os.system(f"kill -9 {pid}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "off"))
        self.label_2.setText(_translate("MainWindow", "on"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())