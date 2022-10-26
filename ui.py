from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(315, 154)
        mainWindow.setMinimumSize(QtCore.QSize(315, 154))
        mainWindow.setMaximumSize(QtCore.QSize(315, 154))
        font = QtGui.QFont()
        font.setPointSize(22)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet("background-color:rgb(161, 174, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 3px solid #e22929;\n"
                                      "border-radius: 6px")
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(120, 90, 41, 41))
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 3px solid #e22929;\n"
                                      "border-radius: 6px")
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border: 3px solid #e22929;\n"
                                   "border-radius: 6px")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(12, 20, 291, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 3px solid #e22929;\n"
                                    "border-radius: 6px")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.raise_()
        self.label_2.raise_()
        self.toolButton.raise_()
        self.lineEdit.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "YouTube"))
        self.pushButton.setText(_translate("mainWindow", "Start"))
        self.toolButton.setText(_translate("mainWindow", "..."))
        self.label_2.setText(_translate("mainWindow", "Save as:"))
