from PyQt6.QtWidgets import QGraphicsOpacityEffect
from PyQt6.QtGui import QMovie, QPixmap, QBrush, QImage, QPainter, QPixmap, QWindow
from PyQt6.QtCore import QPropertyAnimation, QByteArray, Qt
from component import resource_path


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
        movie.setCacheMode(QMovie.CacheMode.CacheAll)
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

    def mask_image(self, imgdata, imgtype='jpeg'):
        image = QImage.fromData(imgdata, imgtype)
        image.scaled(201, 145)
        image.convertToFormat(QImage.Format.Format_ARGB32)
        out_img = QImage(image.width(), image.height(), QImage.Format.Format_ARGB32)
        out_img.fill(Qt.GlobalColor.transparent)

        radius = int((image.width() / 201) * 15)
        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawRoundedRect(0, 0,
                                image.width(), image.height(),
                                radius, radius)

        painter.drawRect(0, radius, image.width(), image.height())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.end()

        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)

        pm = pm.scaled(int(QWindow().devicePixelRatio()) * 201, int(QWindow().devicePixelRatio()) * 145,
                       Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        return pm
