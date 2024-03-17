import sys
from gui.AUDIOINI import AudioPlayer
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QTabWidget)
from Helper.Stile_Sheets import ( TableWidget_style_L, QWidget_style_L)

 
# ИНИЦИАЛИЗАЦИя ПРОГРАММЫ 
class MainWindow(QMainWindow):

    # инициализация программы
    def __init__(self):
        super().__init__()
        self.initUI()

    # инициализация интерфейса
    def initUI(self):
        self.setWindowTitle('FLAKS')

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(TableWidget_style_L)

        tab14 = AudioPlayer()
        tab14.setStyleSheet(QWidget_style_L)

        self.tabs.addTab(tab14, "Audio process")

        self.setCentralWidget(self.tabs)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

