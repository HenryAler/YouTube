from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from ui import Ui_mainWindow
from pytube import YouTube


class MainProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainProject, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.download_video)
        self.ui.lineEdit.setFocus()
        self.ui.progressBar.setValue(0)

    def download_video(self):

        try:
            path = QFileDialog.getExistingDirectory(self, "Выбрать папку", "/", options=QFileDialog.ShowDirsOnly)
            url = self.ui.lineEdit.text()
            yt = YouTube(url)
            title = yt.title
            yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(
                f"{path}")
            self.ui.label.setText("Downloaded..." + title)
            self.ui.progressBar.setValue(100)
            return title
        except Exception:
            self.ui.label.setText("Некорректная ссылка")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    rex = MainProject()
    rex.show()
    sys.exit(app.exec_())
