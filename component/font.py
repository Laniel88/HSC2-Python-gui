from PyQt5.QtGui import QFont, QFontDatabase
from component import resource_path


class Font():
    def addFontDatabase(self):
        QFontDatabase.addApplicationFont(
            resource_path('fonts/D2Coding.ttf'))
        QFontDatabase.addApplicationFont(
            resource_path('fonts/NotoSansKR-Bold.otf'))
        QFontDatabase.addApplicationFont(
            resource_path('fonts/NotoSansKR-Regular.otf'))

    def addFontWithPixel(self, pixel, font="D2Coding", bold=False):
        font = QFont(font)
        font.setPixelSize(pixel)
        if bold == True:
            font.setBold(True)
        font.setHintingPreference(QFont.PreferNoHinting)
        return font
