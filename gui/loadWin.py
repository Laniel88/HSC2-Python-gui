import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from web.webScroll import getAllreList
from setup import resource_path
from gui.mainWin import MainWin

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

        self.worker = WebWorker(Qapp)
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
        QtTest.QTest.qWait(1000)  # delete this
        result = self.exitMsgBox(title, text)
        if result == QMessageBox.Yes:
            print('yes')
            sys.exit(self.app.exit())
        else:
            self.mainWinObj = MainWin((False, False))
            self.mainWinObj.show()

    def exitMsgBox(self, title, text):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('HSC2 :: Exit')
        msgBox.setWindowIcon(QIcon(resource_path('img/ICON.png')))
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(title)
        msgBox.setInformativeText(text)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Yes)
        return msgBox.exec_()

    @pyqtSlot(tuple)
    def connect_mainWin(self, reInfo):
        if reInfo[1] == (0, 0, 0):
            self.exitLoad()
        elif reInfo[0] == 'WEB ERROR':
            self.exitLoad("[HSC2] ERROR",
                          'WEB ERROR\n(ERR CONTENT) ' + reInfo[1])
        else:
            self.close()
            self.mainWinObj = MainWin(reInfo)
            self.mainWinObj.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aW = LoadWin(app)
    app.exec_()
