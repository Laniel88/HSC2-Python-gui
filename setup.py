from gui.loadWin import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aW = loadWin(app)
    app.exec_()