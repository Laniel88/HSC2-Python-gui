import os
import ssl
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *   #[Qpixmap] included
from PyQt5.QtCore    import *
from PyQt5           import uic, QtTest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from web.webScroll import getAllreList
from setup import resource_path

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')

from_class_main = uic.loadUiType(resource_path("'layouts/mainWin.ui"))[0]

class MainWin(QMainWindow, from_class_main):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)