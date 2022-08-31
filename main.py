import sys
import multiprocessing
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from gui.loadWin import LoadWin

if __name__ == "__main__":

    multiprocessing.freeze_support()    # for windows exe (pyinstaller)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    aW = LoadWin(app)
    app.exec_()
