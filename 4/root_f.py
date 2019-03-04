from PyQt5 import QtWidgets
from root import Ui_root
from PyQt5.QtCore import QTimer


class rootwindow(QtWidgets.QMainWindow,Ui_root):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


