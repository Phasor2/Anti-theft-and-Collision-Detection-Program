# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passcode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_passcode(object):
    def setupUi(self, passcode):
        passcode.setObjectName("passcode")
        passcode.resize(1429, 951)
        passcode.setStyleSheet("background-image: url(\'a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(passcode)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.backtomainmenu_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtomainmenu_button.sizePolicy().hasHeightForWidth())
        self.backtomainmenu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.backtomainmenu_button.setFont(font)
        self.backtomainmenu_button.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.backtomainmenu_button.setObjectName("backtomainmenu_button")
        self.verticalLayout.addWidget(self.backtomainmenu_button)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("color: Black;\n"
"font: 75 220pt \"Ubuntu\";")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Num_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_7.sizePolicy().hasHeightForWidth())
        self.Num_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_7.setFont(font)
        self.Num_7.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_7.setObjectName("Num_7")
        self.gridLayout.addWidget(self.Num_7, 0, 0, 1, 1)
        self.Num_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_8.sizePolicy().hasHeightForWidth())
        self.Num_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_8.setFont(font)
        self.Num_8.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_8.setObjectName("Num_8")
        self.gridLayout.addWidget(self.Num_8, 0, 1, 1, 1)
        self.Num_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_9.sizePolicy().hasHeightForWidth())
        self.Num_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_9.setFont(font)
        self.Num_9.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_9.setObjectName("Num_9")
        self.gridLayout.addWidget(self.Num_9, 0, 2, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 0, 3, 1, 1)
        self.Num_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_4.sizePolicy().hasHeightForWidth())
        self.Num_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_4.setFont(font)
        self.Num_4.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_4.setObjectName("Num_4")
        self.gridLayout.addWidget(self.Num_4, 1, 0, 1, 1)
        self.Num_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_5.sizePolicy().hasHeightForWidth())
        self.Num_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_5.setFont(font)
        self.Num_5.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_5.setObjectName("Num_5")
        self.gridLayout.addWidget(self.Num_5, 1, 1, 1, 1)
        self.Num_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_6.sizePolicy().hasHeightForWidth())
        self.Num_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_6.setFont(font)
        self.Num_6.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_6.setObjectName("Num_6")
        self.gridLayout.addWidget(self.Num_6, 1, 2, 1, 1)
        self.Num_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_0.sizePolicy().hasHeightForWidth())
        self.Num_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_0.setFont(font)
        self.Num_0.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_0.setObjectName("Num_0")
        self.gridLayout.addWidget(self.Num_0, 1, 3, 1, 1)
        self.Num_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_1.sizePolicy().hasHeightForWidth())
        self.Num_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_1.setFont(font)
        self.Num_1.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_1.setObjectName("Num_1")
        self.gridLayout.addWidget(self.Num_1, 2, 0, 1, 1)
        self.Num_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_2.sizePolicy().hasHeightForWidth())
        self.Num_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_2.setFont(font)
        self.Num_2.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_2.setObjectName("Num_2")
        self.gridLayout.addWidget(self.Num_2, 2, 1, 1, 1)
        self.Num_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Num_3.sizePolicy().hasHeightForWidth())
        self.Num_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Num_3.setFont(font)
        self.Num_3.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.Num_3.setObjectName("Num_3")
        self.gridLayout.addWidget(self.Num_3, 2, 2, 1, 1)
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_button.sizePolicy().hasHeightForWidth())
        self.enter_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.enter_button.setObjectName("enter_button")
        self.gridLayout.addWidget(self.enter_button, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 7)
        self.verticalLayout.setStretch(3, 7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        passcode.setCentralWidget(self.centralwidget)

        self.retranslateUi(passcode)
        QtCore.QMetaObject.connectSlotsByName(passcode)

    def retranslateUi(self, passcode):
        _translate = QtCore.QCoreApplication.translate
        passcode.setWindowTitle(_translate("passcode", "passcode"))
        self.backtomainmenu_button.setText(_translate("passcode", "Back to MainMenu"))
        self.label_2.setText(_translate("passcode", "ENTER PASSCODE"))
        self.Num_7.setText(_translate("passcode", "7"))
        self.Num_8.setText(_translate("passcode", "8"))
        self.Num_9.setText(_translate("passcode", "9"))
        self.back_button.setText(_translate("passcode", "BACK"))
        self.Num_4.setText(_translate("passcode", "4"))
        self.Num_5.setText(_translate("passcode", "5"))
        self.Num_6.setText(_translate("passcode", "6"))
        self.Num_0.setText(_translate("passcode", "0"))
        self.Num_1.setText(_translate("passcode", "1"))
        self.Num_2.setText(_translate("passcode", "2"))
        self.Num_3.setText(_translate("passcode", "3"))
        self.enter_button.setText(_translate("passcode", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    passcode = QtWidgets.QMainWindow()
    ui = Ui_passcode()
    ui.setupUi(passcode)
    passcode.show()
    sys.exit(app.exec_())

