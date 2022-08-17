import os
import sys
import ssl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from gui.loadWin import LoadWin

if __name__ == "__main__":
    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
    ctx.set_ciphers('SSLv3')

    app = QApplication(sys.argv)

    aW = LoadWin(app)
    app.exec_()
