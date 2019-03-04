# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'root.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(1279, 826)
        root.setStyleSheet(" background-image: url(\'/home/phong/Desktop/antitheft/GUI/3/a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.backtomainmenu_button2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtomainmenu_button2.sizePolicy().hasHeightForWidth())
        self.backtomainmenu_button2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.backtomainmenu_button2.setFont(font)
        self.backtomainmenu_button2.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.backtomainmenu_button2.setObjectName("backtomainmenu_button2")
        self.horizontalLayout_3.addWidget(self.backtomainmenu_button2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setStyleSheet("color:blue;\n"
"border: 3px solid red;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_car_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_car_button.sizePolicy().hasHeightForWidth())
        self.start_car_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.start_car_button.setFont(font)
        self.start_car_button.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.start_car_button.setObjectName("start_car_button")
        self.horizontalLayout.addWidget(self.start_car_button)
        self.manage_drivers_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manage_drivers_button.sizePolicy().hasHeightForWidth())
        self.manage_drivers_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.manage_drivers_button.setFont(font)
        self.manage_drivers_button.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.manage_drivers_button.setObjectName("manage_drivers_button")
        self.horizontalLayout.addWidget(self.manage_drivers_button)
        self.review_footage_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.review_footage_button.sizePolicy().hasHeightForWidth())
        self.review_footage_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.review_footage_button.setFont(font)
        self.review_footage_button.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.review_footage_button.setObjectName("review_footage_button")
        self.horizontalLayout.addWidget(self.review_footage_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "root"))
        self.backtomainmenu_button2.setText(_translate("root", "Back to MainMenu"))
        self.label.setText(_translate("root", "ROOT ADMIN MENU"))
        self.start_car_button.setText(_translate("root", "Start Car"))
        self.manage_drivers_button.setText(_translate("root", "Manage Drivers"))
        self.review_footage_button.setText(_translate("root", "Review Footage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())

