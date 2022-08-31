import os
import ssl
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # [Qpixmap] included
from PyQt5.QtCore import *
from PyQt5 import uic, QtTest

from web import getAllreList
from component import Graphics, Font, resource_path, exitMsgBox
from component import MainGroupClass


form_class_main = uic.loadUiType(resource_path("layouts/mainWin.ui"))[0]

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')


class MainWin(QMainWindow, Graphics, Font, MainGroupClass, form_class_main):

    button_unselected = """
    QPushButton{
        border: none;
        border-radius: 4px;
        color: rgb(255, 255, 255);
        text-align: left;
    }
    QPushButton::hover{
        background-color: rgb(66, 65, 94);
    }
    """

    button_selected = """
    QPushButton{
        border: none;
        border-radius: 4px;
        background-color: rgb(44, 44, 70);
        color: rgb(255, 255, 255);
        text-align: left;
    }
    """

    def __init__(self, Qapp, infoTuple):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.initWidget()
        self.hideAll()

        self.app = Qapp

        self.reLabel = ['학생 식당', '생활과학관', '신소재공학관']

        self.reList = infoTuple[0]
        self.reNum = infoTuple[1]

        # checkData and Load Data (final) , this function includes self.show()
        self.checkLoadData()

    def initUI(self):

        self.setFixedSize(1212, 711)

        self.setWindowTitle('HSC2')
        self.setWindowIcon(QIcon(resource_path('img/ICON.png')))

        # set window center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.addFontDatabase()

        self.buttonA.clicked.connect(self.loadmainA)
        self.buttonB.clicked.connect(self.loadmainB)
        self.buttonC.clicked.connect(self.loadmainC)
        self.refreshButton.clicked.connect(self.refreshMain)

        self.refreshLabel.setFont(
            self.addFontWithPixel(14, 'Noto Sans KR', True))

    # Set text for timeLabel
    def loadTimeLabel(self):
        self.timeLabel_Date.setText(
            QDateTime.currentDateTime().toString('yyyy.MM.dd')
        )

        self.timeLabel_Time.setText(
            QTime.currentTime().toString('AP hh:mm:ss')
        )

    # Exit unconditionally if unKnown Error accured
    def errorExit(self, label="UNKNOWN ERROR"):
        exitMsgBox('ERROR while loading Menu', label, QMessageBox.Yes)
        sys.exit(self.app.exit())

    # Check if the received data is normal
    def checkLoadData(self):
        # If there is no data to load (sunday, failed to load data)
        if (self.reList, self.reNum) == (False, (0, 0, 0)):
            self.nonDataLoad()
        # If each restaurant has 'non-business' data (holiday)
        elif self.reNum == (1, 1, 1) and self.reList[0][0][0] == 'https://www.hanyang.ac.kr/html-repositories/images/custom/food/no-img.jpg':
            self.nonBusiness()
        # Normal operation
        else:
            self.loadData()

    ##<--------    connected from checkLoadData()     ------------>##

    def nonDataLoad(self):
        self.menuBarSettings()
        self.mainLoadAnimation()
        self.show()
        self.autoLoad()

    def loadData(self):
        self.menuBarSettings()
        self.mainLoadAnimation()
        self.show()
        self.autoLoad()

    def nonBusiness(self):
        self.menuBarSettings()
        self.mainLoadAnimation()
        self.autoLoad()
        self.show()
    ## <-----------------------          ------------------------> ##

    def autoLoad(self):
        time = int(QTime.currentTime().toString('hh'))
        # before 2 p.m '중식'
        if time < 14:
            self.loadmainA()
        elif time < 16:
            self.loadmainB()
        else:
            self.loadmainC()

    def loadmainA(self):
        self.buttonA.setStyleSheet(MainWin.button_selected)
        self.buttonB.setStyleSheet(MainWin.button_unselected)
        self.buttonC.setStyleSheet(MainWin.button_unselected)
        self.fade(self.mainGroup, 400)
        QtTest.QTest.qWait(500)
        self.hideAll()
        reNum = self.loadmainGroup('중식')
        self.unfade(self.mainGroup, 400)
        QtTest.QTest.qWait(400)
        if reNum == 0:
            self.emptyMain()

    def loadmainB(self):
        self.buttonA.setStyleSheet(MainWin.button_unselected)
        self.buttonB.setStyleSheet(MainWin.button_selected)
        self.buttonC.setStyleSheet(MainWin.button_unselected)
        self.fade(self.mainGroup, 400)
        QtTest.QTest.qWait(500)
        self.hideAll()
        reNum = self.loadmainGroup('분식')
        self.unfade(self.mainGroup, 400)
        QtTest.QTest.qWait(400)
        if reNum == 0:
            self.emptyMain()

    def loadmainC(self):
        self.buttonA.setStyleSheet(MainWin.button_unselected)
        self.buttonB.setStyleSheet(MainWin.button_unselected)
        self.buttonC.setStyleSheet(MainWin.button_selected)
        self.fade(self.mainGroup, 400)
        QtTest.QTest.qWait(500)
        self.hideAll()
        reNum = self.loadmainGroup('석식')
        self.unfade(self.mainGroup, 400)
        QtTest.QTest.qWait(400)
        if reNum == 0:
            self.emptyMain()

    def refreshMain(self):
        os.environ["QT_SCALE_FACTOR"] = "2"
        self.unableButtons()
        self.fade(self.mainGroup, 300)
        QtTest.QTest.qWait(300)
        self.hideAll()
        self.gifStart('img/s_loadGif_trans.gif',
                      QSize(70, 70), self.refreshGif)

        self.worker = WebWorker()
        self.worker.finished.connect(self.connect_check)
        self.worker.start()

        self.refreshGif.show()
        self.refreshLabel.show()
        self.refreshButton.setText('Wait')
        self.refreshLabel.setText('Reloading')
        self.unfade(self.mainGroup, 400)
        QtTest.QTest.qWait(400)

    @pyqtSlot(tuple)
    def connect_check(self, reInfo):
        if reInfo[0] == 'WEB ERROR':
            self.exitLoad('WEB ERROR\n(ERR CONTENT) ' + reInfo[1])
        self.reList = reInfo[0]
        self.reNum = reInfo[1]
        self.refreshGif.setText('')
        self.refreshButton.setText('메뉴 새로고침')
        self.enableButtons()
        self.checkLoadData()

    def emptyMain(self):
        self.setImg('img/xmark.png', self.refreshGif, 70)
        self.refreshLabel.setText('Nothing to Load')
        self.refreshGif.show()
        self.refreshLabel.show()

    def menuBarSettings(self):
        # mB logo setting
        self.setImg('img/mb_logo.png', self.mb_logoLabel, 181)

        # Font Settings
        font = self.addFontWithPixel(14)
        for buttons in [self.buttonA, self.buttonB, self.buttonC, self.refreshButton]:
            buttons.setFont(font)

        self.timeLabel_Date.setFont(self.addFontWithPixel(13))
        self.timeLabel_Time.setFont(self.addFontWithPixel(20))
        self.buttonInfoLabel.setFont(self.addFontWithPixel(12))
        self.Info_NameLabel.setFont(self.addFontWithPixel(13))
        self.Info_InfoLabel.setFont(self.addFontWithPixel(12))

        # timeLabel QTimer
        self.timer = QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.loadTimeLabel)

    def unableButtons(self):
        for button in [self.buttonA, self.buttonB, self.buttonC, self.refreshButton]:
            button.setEnabled(False)

    def enableButtons(self):
        for button in [self.buttonA, self.buttonB, self.buttonC, self.refreshButton]:
            button.setEnabled(True)


class WebWorker(QThread):
    finished = pyqtSignal(tuple)

    def run(self):
        self.finished.emit(getAllreList())
