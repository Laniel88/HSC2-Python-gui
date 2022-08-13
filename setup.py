from PyQt5.QtWidgets import QMessageBox, QGraphicsOpacityEffect
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QPropertyAnimation, QByteArray, QSize


# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)


def resource_path(relative_path):
    """ Used for developing"""
    return 'res/' + relative_path  # os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+


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


class Animation():
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
