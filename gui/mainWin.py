import os
import ssl
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # [Qpixmap] included
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from web.webScroll import getAllreList
from setup import resource_path

form_class_main = uic.loadUiType(resource_path("layouts/mainWin.ui"))[0]


class MainWin(QMainWindow, form_class_main):

    def __init__(self, infoTuple):
        super().__init__()
        self.setupUi(self)

        self.reList = infoTuple[0]
        self.reNum = infoTuple[1]

        self.initUI()

    def initUI(self):

        self.setFixedHeight(800)
        self.setMaximumWidth(1600)
        self.setMinimumSize(1000, 800)

        self.setWindowTitle('HSC2')
        self.setWindowIcon(QIcon(resource_path('ICON.png')))

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
