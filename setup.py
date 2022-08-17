from urllib import request
from PyQt5.QtWidgets import QMessageBox, QGraphicsOpacityEffect
from PyQt5.QtGui import QIcon, QMovie, QFont, QFontDatabase, QPixmap, QBrush, QImage, QPainter, QPixmap, QWindow
from PyQt5.QtCore import QPropertyAnimation, QByteArray, Qt

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)


def resource_path(relative_path):
    """ Used for developing"""
    return 'res/' + relative_path


def getRequestsInfinite(url):
    try:
        response = request.urlopen(url)
        return response
    except:
        return getRequestsInfinite(url)


def printReInfo(infoList, cntTuple):
    print('printing reInfo : {}'.format(cntTuple))
    for i in range(3):
        for j in range(len(infoList[i])):
            print(infoList[i][j])


def exitMsgBox(title, text, buttons=QMessageBox.Yes | QMessageBox.Ignore):
    msgBox = QMessageBox()
    msgBox.setWindowTitle('HSC2 :: Exit')
    msgBox.setWindowIcon(QIcon(resource_path('img/ICON.png')))
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(title)
    msgBox.setInformativeText(text)
    msgBox.setStandardButtons(buttons)
    msgBox.setDefaultButton(QMessageBox.Yes)
    return msgBox.exec_()


def setUpMenuGroup():
    print("fill up!")


class Graphics():
    # fading animation
    def fade(self, widget, duration=1000):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget, duration=1000):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def gifStart(self, path, size, object):
        movie = QMovie(resource_path(path), QByteArray(), self)
        movie.setCacheMode(QMovie.CacheAll)
        movie.setScaledSize(size)
        object.setMovie(movie)
        movie.start()

    def mainLoadAnimation(self):
        self.unfade(self.mainGroup)

    def setImg(self, imgPath, object, Width):
        qPixmapVar = QPixmap()
        qPixmapVar.load(resource_path(imgPath))
        qPixmapVar = qPixmapVar.scaledToWidth(Width)
        object.setPixmap(qPixmapVar)

    def mask_image(self, imgdata, imgtype='png'):

        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)

        out_img = QImage(image.width(), image.height(), QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        radius = int((image.width() / 201) * 15)

        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(0, 0,
                                image.width(), image.height(),
                                radius, radius)

        painter.drawRect(0, radius, image.width(), image.height())
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.end()

        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)

        pm = pm.scaled(QWindow().devicePixelRatio() * 201, QWindow().devicePixelRatio() * 145,
                       Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pm


class Font():
    def addFontDatabase(self):
        QFontDatabase.addApplicationFont(resource_path('fonts/D2Coding.ttf'))
        QFontDatabase.addApplicationFont(
            resource_path('fonts/NotoSansKR-Bold.otf'))
        QFontDatabase.addApplicationFont(
            resource_path('fonts/NotoSansKR-Medium.otf'))
        QFontDatabase.addApplicationFont(
            resource_path('fonts/NotoSansKR-Regular.otf'))

    def addFontWithPixel(self, pixel, font="D2Coding", bold=False):
        font = QFont(font)
        font.setPixelSize(pixel)
        if bold == True:
            font.setBold(True)
        font.setHintingPreference(QFont.PreferNoHinting)
        return font
