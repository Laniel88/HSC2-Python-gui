import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *   
from PyQt5.QtCore    import *
from PyQt5           import uic, QtTest

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

def resource_path(relative_path):
    """ Used for developing"""
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/res/'+relative_path

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)     #enable highdpi scaling
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,    True)        #use highdpi icons

from_class = uic.loadUiType(resource_path('layouts/loadWin.ui'))[0]

# class Worker(QThread):
#     finished = pyqtSignal(tuple)
#     def run(self):
#         self.mainWin = MainWindowSeq()
#         menuTu = self.mainWin.scrollDIC()
#         self.finished.emit(menuTu)

class loadWin(QMainWindow, from_class) :
    
    def __init__(self, Qapp) :
        super().__init__()
        self.initUI()

        self.app = Qapp     #object 전달

        self.backgroundImg()
        self.loadGif()
        self.show()
        self.exitLoad()
    
    def initUI(self):
        self.setupUi(self) 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()           #center arrangement
        self.resize(540, 400)  #size : 540 x 400
        self.setWindowIcon(QIcon(resource_path('img/ICON.png')))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def backgroundImg(self):
        qPixmapVar = QPixmap()      #Create QPixmap object
        qPixmapVar.load(resource_path('img/loadMain.png'))
        qPixmapVar = qPixmapVar.scaledToWidth(540)
        self.loadMain.setPixmap(qPixmapVar)
    
    def loadGif(self):
        movie = QMovie(resource_path('img/s_loadGif.gif'), QByteArray(), self)
        movie.setCacheMode(QMovie.CacheAll)
        movie.setScaledSize(QSize(40,40))
        self.loadGif_s.setMovie(movie)
        movie.start()



    def exitLoad(self):
        QtTest.QTest.qWait(1000) #delete this
        result = self.exitMsgBox()
        if result == QMessageBox.Yes:
            print('yes')
            sys.exit(self.app.exit())

    def exitMsgBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('HSC2 :: Exit')
        msgBox.setWindowIcon(QIcon(resource_path('img/ICON.png')))
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Nothing to Load')
        msgBox.setInformativeText('All cafeteria is closed')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Yes)
        return msgBox.exec_()
    
 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    aW = loadWin()
    app.exec_()