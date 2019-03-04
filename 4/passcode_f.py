from PyQt5 import QtWidgets
from passcode import Ui_passcode
from PyQt5.QtWidgets import QApplication
import sys


class passcodewindow(QtWidgets.QMainWindow,Ui_passcode):

    def backspacecode(self):
        self.lineEdit.backspace()

    def appendcode(self,n):
        self.lineEdit.insert(str(n))
        self.lineEdit.setEchoMode(2)


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Button instantiation
        self.Num_0.clicked.connect(lambda: self.appendcode(0))
        self.Num_1.clicked.connect(lambda: self.appendcode(1))
        self.Num_2.clicked.connect(lambda: self.appendcode(2))
        self.Num_3.clicked.connect(lambda: self.appendcode(3))
        self.Num_4.clicked.connect(lambda: self.appendcode(4))
        self.Num_5.clicked.connect(lambda: self.appendcode(5))
        self.Num_6.clicked.connect(lambda: self.appendcode(6))
        self.Num_7.clicked.connect(lambda: self.appendcode(7))
        self.Num_8.clicked.connect(lambda: self.appendcode(8))
        self.Num_9.clicked.connect(lambda: self.appendcode(9))

        self.back_button.clicked.connect(self.backspacecode)

#app = QApplication(sys.argv)
#passcode=passcodewindow()
#passcode.show()

#sys.exit(app.exec_())

