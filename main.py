import sys
import ssl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from gui.loadWin import LoadWin

if __name__ == "__main__":

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
    ctx.set_ciphers('SSLv3')

    app = QApplication(sys.argv)
    aW = LoadWin(app)
    app.exec_()
