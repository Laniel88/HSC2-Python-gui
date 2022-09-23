from PyQt6.QtWidgets import QMessageBox, QDialogButtonBox
from PyQt6.QtGui import QIcon
from component import resource_path


def exitMsgBox(title, text, buttons=QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.Ignore):
    msgBox = QMessageBox()
    msgBox.setWindowTitle('HSC2 :: Exit')
    msgBox.setWindowIcon(QIcon(resource_path('img/ICON.png')))
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.setText(title)
    msgBox.setInformativeText(text)
    msgBox.setStandardButtons(buttons)
    msgBox.setDefaultButton(QDialogButtonBox.StandardButton.Yes)
    return msgBox.exec_()

# # print final data
# def printReInfo(infoList, cntTuple):
#     print('printing reInfo : {}'.format(cntTuple))
#     for i in range(3):
#         for j in range(len(infoList[i])):
#             print(infoList[i][j])
