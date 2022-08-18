import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

from web import getAllreList
from component import resource_path, exitMsgBox
from gui import MainWin

form_class = uic.loadUiType(resource_path('layouts/loadWin.ui'))[0]


class WebWorker(QThread):
    finished = pyqtSignal(tuple)

    def run(self):
        self.finished.emit(getAllreList())


class LoadWin(QMainWindow, form_class):

    def __init__(self, Qapp):
        super().__init__()
        self.initUI()

        self.app = Qapp  # object 전달

        self.backgroundImg()
        self.loadGif()
        self.show()

        self.worker = WebWorker()
        self.worker.finished.connect(self.connect_mainWin)
        self.worker.start()

    def initUI(self):
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()  # center arrangement
        self.resize(540, 400)  # size : 540 x 400
        self.setWindowIcon(QIcon(resource_path('img/ICON.png')))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def backgroundImg(self):
        qPixmapVar = QPixmap()
        qPixmapVar.load(resource_path('img/loadMain.png'))
        qPixmapVar = qPixmapVar.scaledToWidth(540)
        self.loadMain.setPixmap(qPixmapVar)

    def loadGif(self):
        movie = QMovie(resource_path('img/s_loadGif.gif'), QByteArray(), self)
        movie.setCacheMode(QMovie.CacheAll)
        movie.setScaledSize(QSize(40, 40))
        self.loadGif_s.setMovie(movie)
        movie.start()

    def exitLoad(self, title='Nothing to Load', text='All cafeteria is closed'):
        result = exitMsgBox(title, text)
        if result == QMessageBox.Yes:
            print('yes')
            sys.exit(self.app.exit())
        else:
            self.close()
            self.mainWinObj = MainWin(self.app, (False, False))

    @pyqtSlot(tuple)
    def connect_mainWin(self, reInfo):
        if reInfo[1] == (0, 0, 0):
            self.exitLoad()
        elif reInfo[0] == 'WEB ERROR':
            self.exitLoad("[HSC2] ERROR",
                          'WEB ERROR\n(ERR CONTENT) ' + reInfo[1])
        else:
            self.close()
            self.mainWinObj = MainWin(self.app, reInfo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aW = LoadWin(app)
    app.exec_()
