# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_a_driver.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remove_a_driver(object):
    def setupUi(self, remove_a_driver):
        remove_a_driver.setObjectName("remove_a_driver")
        remove_a_driver.resize(1190, 893)
        font = QtGui.QFont()
        font.setFamily("wasy10")
        remove_a_driver.setFont(font)
        remove_a_driver.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(remove_a_driver)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.left.setFont(font)
        self.left.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.left.setObjectName("left")
        self.horizontalLayout.addWidget(self.left)
        self.preview_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_image.sizePolicy().hasHeightForWidth())
        self.preview_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.preview_image.setFont(font)
        self.preview_image.setStyleSheet("color:white;\n"
"")
        self.preview_image.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_image.setObjectName("preview_image")
        self.horizontalLayout.addWidget(self.preview_image)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.right.setFont(font)
        self.right.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.right.setObjectName("right")
        self.horizontalLayout.addWidget(self.right)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_label.sizePolicy().hasHeightForWidth())
        self.id_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color:white;\n"
"")
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName("id_label")
        self.verticalLayout.addWidget(self.id_label)
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.remove.setFont(font)
        self.remove.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 8)
        self.verticalLayout.setStretch(4, 1)
        remove_a_driver.setCentralWidget(self.centralwidget)

        self.retranslateUi(remove_a_driver)
        QtCore.QMetaObject.connectSlotsByName(remove_a_driver)

    def retranslateUi(self, remove_a_driver):
        _translate = QtCore.QCoreApplication.translate
        remove_a_driver.setWindowTitle(_translate("remove_a_driver", "remove a driver"))
        self.back.setText(_translate("remove_a_driver", "Back to Manage Drivers"))
        self.label_3.setText(_translate("remove_a_driver", "Remove a Driver"))
        self.left.setText(_translate("remove_a_driver", "⊲"))
        self.preview_image.setText(_translate("remove_a_driver", "Preview Image"))
        self.right.setText(_translate("remove_a_driver", "⊳"))
        self.id_label.setText(_translate("remove_a_driver", "ID: 1/18"))
        self.remove.setText(_translate("remove_a_driver", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remove_a_driver = QtWidgets.QMainWindow()
    ui = Ui_remove_a_driver()
    ui.setupUi(remove_a_driver)
    remove_a_driver.show()
    sys.exit(app.exec_())

