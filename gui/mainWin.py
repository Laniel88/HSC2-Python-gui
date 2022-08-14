import os
from re import S
import ssl
import sys
from urllib import request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # [Qpixmap] included
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from setup import *

form_class_main = uic.loadUiType(resource_path("layouts/mainWin.ui"))[0]

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')


class MainWin(QMainWindow, Graphics, Font, form_class_main):

    def __init__(self, Qapp, infoTuple):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # self.initWidget()

        self.app = Qapp

        self.reLabel = ['학생식당', '생활과학관 식당', '신소재공학관 식당']

        self.reList = infoTuple[0]
        self.reNum = infoTuple[1]

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
        self.loadMenuBar()
        self.mainGroupSetting()
        self.show()
        self.mainLoadAnimation()

    def loadData(self):
        printReInfo(self.reList, self.reNum)
        self.loadMenuBar()
        self.unfade(self.menuBar, 1700)
        self.unfade(self.mainGroup, 1700)

        self.gifStart('img/s_loadGif_trans.gif',
                      QSize(70, 70), self.refreshGif)
        self.show()

    ## <-----                         -----> ##
    def loadMenuBar(self):
        self.setImg('img/mb_logo.png', self.mb_logoLabel, 181)
        self.menuBarSettings()

    def mainGroupSetting(self):
        # creating a QGraphicsDropShadowEffect object
        shadow = QGraphicsDropShadowEffect()

        # setting blur radius
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(40, 40, 40).darker())
        shadow.setOffset(8)
        # adding shadow to the label
        self.listOfMenuGroup1.setGraphicsEffect(shadow)

        url = 'https://www.hanyang.ac.kr/web/www/re2?p_p_id=foodView_WAR_foodportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2&_foodView_WAR_foodportlet_fileId=896904&_foodView_WAR_foodportlet_cmd=download&_foodView_WAR_foodportlet_sFoodDateYear=2022&_foodView_WAR_foodportlet_sFoodDateMonth=7&_foodView_WAR_foodportlet_action=view&_foodView_WAR_foodportlet_sFoodDateDay=9'
        img = request.urlopen(url).read()
        qPixVar = self.mask_image(img, 'jpeg')
        self.menuImage_1.setPixmap(qPixVar)

    def menuBarSettings(self):
        # Font Settings
        font = self.addFontWithPixel(14)
        for buttons in [self.buttonA, self.buttonB, self.buttonC, self.refreshButton]:
            buttons.setFont(font)

        self.timeLabel_Date.setFont(self.addFontWithPixel(13))
        self.timeLabel_Time.setFont(self.addFontWithPixel(20))
        self.buttonInfoLabel.setFont(self.addFontWithPixel(12))
        self.Info_NameLabel.setFont(self.addFontWithPixel(13))
        self.Info_InfoLabel.setFont(self.addFontWithPixel(12))       # 9point
        # Make sure that the font size is appropriate & correct font size

        # timeLabel QTimer
        self.timer = QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.loadTimeLabel)

    # check if instance tuple attribute is initialized

    def test_loadMenu(self, labelIndex, menu, listOfMenuGroup):
        # format title
        titleLabel = '[{}]'.format(self.reLabel(labelIndex)) if menu[1][0] == False \
            else '[{}] :: {}'.format(self.reLabel(labelIndex), menu[1][0])

        # set titleLabel
        listOfMenuGroup[1].setStyleSheet()
        listOfMenuGroup[1].setText(titleLabel)
        listOfMenuGroup[1].setAlignment(Qt.AlignLeft)

        # set(load) menuImage
        self.qPix.loadFromData(request.urlopen(
            menu[0][0] + '#jpeg', context=ctx).read())
        self.qPix = self.qPix.scaledToWidth(205)
        listOfMenuGroup[2].setPixmap(self.qPix)

    # Initialize the widget and save it as a tuple in the instance attribute
    def initWidget(self):
        # MenuGroupA - 중식
        self.listOfMenuGroup1 = (self.MenuGroup_1, self.titleLabel_1, self.menuImage_1,
                                 self.menuLabel_1, self.priceLabel_1, self.colorLable_1)
        self.listOfMenuGroup2 = (self.MenuGroup_2, self.titleLabel_2, self.menuImage_2,
                                 self.menuLabel_2, self.priceLabel_2, self.colorLable_2)
        self.listOfMenuGroup3 = (self.MenuGroup_3, self.titleLabel_3, self.menuImage_3,
                                 self.menuLabel_3, self.priceLabel_3, self.colorLable_3)
        self.listOfMenuGroup4 = (self.MenuGroup_4, self.titleLabel_4, self.menuImage_4,
                                 self.menuLabel_4, self.priceLabel_4, self.colorLable_4)
        self.listOfMenuGroup5 = (self.MenuGroup_5, self.titleLabel_5, self.menuImage_5,
                                 self.menuLabel_5, self.priceLabel_5, self.colorLable_5)
        self.listOfMenuGroup6 = (self.MenuGroup_6, self.titleLabel_6, self.menuImage_6,
                                 self.menuLabel_6, self.priceLabel_6, self.colorLable_6)
        self.listOfMenuGroup7 = (self.MenuGroup_7, self.titleLabel_7, self.menuImage_7,
                                 self.menuLabel_7, self.priceLabel_7, self.colorLable_7)
        self.listOfMenuGroup8 = (self.MenuGroup_8, self.titleLabel_8, self.menuImage_8,
                                 self.menuLabel_8, self.priceLabel_8, self.colorLable_8)
