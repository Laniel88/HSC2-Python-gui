from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

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
