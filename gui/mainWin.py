import os
import ssl
import sys
import urllib.request

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # [Qpixmap] included
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from setup import Animation, resource_path, printReInfo, exitMsgBox

form_class_main = uic.loadUiType(resource_path("layouts/mainWin.ui"))[0]

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')


class MainWin(QMainWindow, Animation, form_class_main):

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
        self.fontSize = 9

        self.checkLoadData()  # checkData and Load Data

    def initUI(self):

        # self.setFixedHeight(800)
        # self.setMaximumWidth(1600)
        # self.setMinimumSize(1000, 800)
        self.setFixedSize(1264, 711)

        self.setWindowTitle('HSC2')
        self.setWindowIcon(QIcon(resource_path('img/ICON.png')))

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def menuBarSettings(self):
        # Font Settings
        self.menuBarFont()
        # Make sure that the font size is appropriate & correct font size

        # timeLabel QTimer
        self.timer = QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.loadTimeLabel)

        self.Info_NameLabel.setWordWrap(True)

    def menuBarFont(self):
        # Font Settings
        QFontDatabase.addApplicationFont(resource_path('fonts/D2Coding.ttf'))
        font = QFont("D2Coding", self.fontSize + 2)
        for buttons in [self.buttonA, self.buttonB, self.buttonC, self.refreshButton]:
            buttons.setFont(font)
        self.timeLabel_Date.setFont(QFont("D2Coding", self.fontSize + 2))
        self.timeLabel_Time.setFont(QFont("D2Coding", self.fontSize + 6))
        self.buttonInfoLabel.setFont(QFont("D2Coding", self.fontSize))
        self.Info_NameLabel.setFont(QFont("D2Coding", self.fontSize + 2))
        self.Info_InfoLabel.setFont(QFont("D2Coding", self.fontSize))

    def loadTimeLabel(self):
        # Time Label
        self.timeLabel_Date.setText(
            QDateTime.currentDateTime().toString('yyyy.MM.dd')
        )

        self.timeLabel_Time.setText(
            QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
        )

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
        self.loadMenuBar()
        self.unfade(self.menuBar, 1700)  # fade pre-run

        self.gifStart('img/s_loadGif_trans.gif',
                      QSize(70, 70), self.refreshGif)
        self.menuBarSettings()

        self.show()

        print(self.Info_NameLabel.text())

    ## <-----                         -----> ##
    def loadMenuBar(self):
        self.qPix.load(resource_path('img/mb_logo.png'))
        self.qPix = self.qPix.scaledToWidth(181)
        self.mb_logoLabel.setPixmap(self.qPix)

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
        self.qPix.loadFromData(urllib.request.urlopen(
            menu[0][0] + '#jpeg', context=ctx).read())
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
