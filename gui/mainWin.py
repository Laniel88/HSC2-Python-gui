import os
import ssl
import sys
import urllib.request

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # [Qpixmap] included
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from setup import resource_path, printReInfo, exitMsgBox

form_class_main = uic.loadUiType(resource_path("layouts/mainWin.ui"))[0]

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')

class MainWin(QMainWindow, form_class_main):

    def __init__(self, Qapp, infoTuple):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # self.initWidget()

        self.app = Qapp
        self.qPix = QPixmap()

        self.reLabel = ['학생식당', '생활과학관 식당', '신소재공학관 식당']

        self.reList = infoTuple[0]
        self.reNum = infoTuple[1]
        self.checkLoadData()  # checkData and Load Data

    def initUI(self):
        # self.
        # self.setFixedHeight(800)
        # self.setMaximumWidth(1600)
        # self.setMinimumSize(1000, 800)

        self.setWindowTitle('HSC2')
        self.setWindowIcon(QIcon(resource_path('ICON.png')))

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    """
    MenuGroup_{NUM}
     ㄴ titleLabel_{NUM}  ;; [식당이름] 정보
     ㄴ menuImage_{NUM}
     ㄴ menuLabel_{NUM}
     ㄴ priceLabel_{NUM}
     
     Numbering) 중식 = A , 간식 = B, 석식 = C
    """
    """
    About MenuGroup
    MAXIMUM : (6,3,4)
    중식 MAX 3+2+3  8개
    간식(학생식당) 3  4개
    석식 MAX 3+1+2  8개  
    """

    ## <-----   Functions for error handling    -----> ##

    def errorExit(self, label):
        exitMsgBox('ERROR while loading Menu', label, QMessageBox.Yes)
        sys.exit(self.app.exit())   # Must shut down unconditionally

    def checkLoadData(self):
        if (self.reList, self.reNum) == (False, False):
            self.nonDataLoad()
        else:
            self.loadData()

    def nonDataLoad(self):
        print('fillOut')

    def loadData(self):
        printReInfo(self.reList, self.reNum)
        self.show()

    # check if instance tuple attribute is initialized
    def test_loadMenu(self, labelIndex, menu, listOfMenuGroup):
        # format title
        titleLabel = '[{}]'.format(self.reLabel(labelIndex)) if menu[1][0] == False \
            else '[{}] :: {}'.format(self.reLabel(labelIndex), menu[1][0])

        # set titleLabel
        listOfMenuGroup[1].setStyleSheet(
            "border-style: solid;"
            "border-width: 2px;")
        listOfMenuGroup[1].setText(titleLabel)
        listOfMenuGroup[1].setAlignment(Qt.AlignLeft)

        # set(load) menuImage
        self.qPix.loadFromData(urllib.request.urlopen(menu[0][0] + '#jpeg', context=ctx).read())
        self.qPix = self.qPix.scaledToWidth(205)
        listOfMenuGroup[2].setPixmap(self.qPix)

        
    # Initialize the widget and save it as a tuple in the instance attribute

    def initWidget(self):
        # MenuGroupA - 중식
        self.listOfMenuGroupA1 = (self.MenuGroup_A1, self.titleLabel_A1, self.menuImage_A1,
                                  self.menuLabel_A1, self.priceLabel_A1)
        self.listOfMenuGroupA2 = (self.MenuGroup_A2, self.titleLabel_A2, self.menuImage_A2,
                                  self.menuLabel_A2, self.priceLabel_A2)
        self.listOfMenuGroupA3 = (self.MenuGroup_A3, self.titleLabel_A3, self.menuImage_A3,
                                  self.menuLabel_A3, self.priceLabel_A3)
        self.listOfMenuGroupA4 = (self.MenuGroup_A4, self.titleLabel_A4, self.menuImage_A4,
                                  self.menuLabel_A4, self.priceLabel_A4)
        self.listOfMenuGroupA5 = (self.MenuGroup_A5, self.titleLabel_A5, self.menuImage_A5,
                                  self.menuLabel_A5, self.priceLabel_A5)
        self.listOfMenuGroupA6 = (self.MenuGroup_A6, self.titleLabel_A6, self.menuImage_A6,
                                  self.menuLabel_A6, self.priceLabel_A6)
        self.listOfMenuGroupA7 = (self.MenuGroup_A7, self.titleLabel_A7, self.menuImage_A7,
                                  self.menuLabel_A7, self.priceLabel_A7)
        self.listOfMenuGroupA8 = (self.MenuGroup_A8, self.titleLabel_A8, self.menuImage_A8,
                                  self.menuLabel_A8, self.priceLabel_A8)

        # MenuGroupB - 간식
        self.listOfMenuGroupB1 = (self.MenuGroup_B1, self.titleLabel_B1, self.menuImage_B1,
                                  self.menuLabel_B1, self.priceLabel_B1)
        self.listOfMenuGroupB2 = (self.MenuGroup_B2, self.titleLabel_B2, self.menuImage_B2,
                                  self.menuLabel_B2, self.priceLabel_B2)
        self.listOfMenuGroupB3 = (self.MenuGroup_B3, self.titleLabel_B3, self.menuImage_B3,
                                  self.menuLabel_B3, self.priceLabel_B3)

        # MenuGroupC - 중식
        self.listOfMenuGroupA1 = (self.MenuGroup_C1, self.titleLabel_C1, self.menuImage_C1,
                                  self.menuLabel_C1, self.priceLabel_C1)
        self.listOfMenuGroupA2 = (self.MenuGroup_C2, self.titleLabel_C2, self.menuImage_C2,
                                  self.menuLabel_C2, self.priceLabel_C2)
        self.listOfMenuGroupA3 = (self.MenuGroup_C3, self.titleLabel_C3, self.menuImage_C3,
                                  self.menuLabel_C3, self.priceLabel_C3)
        self.listOfMenuGroupA4 = (self.MenuGroup_C4, self.titleLabel_C4, self.menuImage_C4,
                                  self.menuLabel_C4, self.priceLabel_C4)
        self.listOfMenuGroupA5 = (self.MenuGroup_C5, self.titleLabel_C5, self.menuImage_C5,
                                  self.menuLabel_C5, self.priceLabel_C5)
        self.listOfMenuGroupA6 = (self.MenuGroup_C6, self.titleLabel_C6, self.menuImage_C6,
                                  self.menuLabel_C6, self.priceLabel_C6)
        self.listOfMenuGroupA7 = (self.MenuGroup_C7, self.titleLabel_C7, self.menuImage_C7,
                                  self.menuLabel_C7, self.priceLabel_C7)
        self.listOfMenuGroupA8 = (self.MenuGroup_C8, self.titleLabel_C8, self.menuImage_C8,
                                  self.menuLabel_C8, self.priceLabel_C8)
