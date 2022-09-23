import sys
from PyQt6.QtWidgets import QApplication
from gui.loadWin import LoadWin

"""
# from PyQt6.QtCore import *
# QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
# QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

The high DPI (dots per inch) scaling attributes:

Qt.AA_EnableHighDpiScaling,
Qt.AA_DisableHighDpiScaling and,
Qt.AA_UseHighDpiPixmaps
 
have been deprecated because high DPI setting is the default setting in PyQt6. This cannot be disabled.
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aW = LoadWin(app)
    app.exec()
