from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("WE WON")
        self.initUI()

    def initUI(self):
        self.slider = QtWidgets.QCheckBox(self)
        self.slider.setText("on")
        self.slider.setChecked(True)
        self.slider.stateChanged.connect(self.mudafich)

        self.slider1 = QtWidgets.QCheckBox(self)
        self.slider1.setText("Quit")
        self.slider1.setChecked(False)
        self.slider1.move(100,0)
        self.slider1.stateChanged.connect(self.end)

    def end(self):
        a=open("closeapp.dat",'w')
        a.write("1")
        a.close()
        quit()
    def mudafich(self):
        if (self.slider.isChecked()):
            a=open("off.dat",'w')
            a.write("1")
            a.close()
        else:
            a=open("off.dat",'w')
            a.write("0")
            a.close()


def window():
    app = QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())
window()