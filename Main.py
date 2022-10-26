from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui import Ui_mainWindow
import requests


class MainProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainProject, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.toolButton.clicked.connect(self.open_dialog)

    def open_dialog(self):
        res = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        print(res)

    def get_files(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    rex = MainProject()
    rex.show()
    sys.exit(app.exec_())