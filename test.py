import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        openDirButton = QPushButton("Open Directory")
        openDirButton.clicked.connect(self.getDirectory)

        layoutV = QVBoxLayout()
        layoutV.addWidget(openDirButton)

        layoutH = QHBoxLayout()
        layoutH.addLayout(layoutV)


        centerWidget = QWidget()
        centerWidget.setLayout(layoutH)
        self.setCentralWidget(centerWidget)

        self.resize(740, 480)
        self.setWindowTitle("PyQt5-QFileDialog")

    def getDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        print(dirlist)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())