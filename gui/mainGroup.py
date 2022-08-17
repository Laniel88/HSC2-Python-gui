import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from setup import resource_path, getRequestsInfinite


class MainGroupClass():
    re_color_list = ('rgb(249,205,173)',
                     'rgb(200,200,169)', 'rgb(156, 158, 254)')

    def loadMenuGroup(self, labelIndex, menuData, listOfMenuGroup):
        # show menuGroup
        listOfMenuGroup[0].show()

        # settings of menuImage
        if menuData[0] == 'https://www.hanyang.ac.kr/html-repositories/images/custom/food/no-img.jpg':
            img = open(resource_path('img/noImage.png'), 'rb').read()
            listOfMenuGroup[3].setPixmap(self.mask_image(img, 'png'))
        else:
            #img = request.urlopen(menuData[0]).read()
            img = getRequestsInfinite(menuData[0]).read()
            listOfMenuGroup[3].setPixmap(self.mask_image(img, 'jpeg'))

        # set titleLabelA
        listOfMenuGroup[1].setText(self.reLabel[labelIndex])
        listOfMenuGroup[1].setStyleSheet(
            'color:' + MainGroupClass.re_color_list[labelIndex])
        listOfMenuGroup[1].setFont(
            self.addFontWithPixel(21, 'Noto Sans KR', True))

        # move titlelabelB
        if labelIndex == 0:
            listOfMenuGroup[2].move(97, 153)
        elif labelIndex == 1:
            listOfMenuGroup[2].move(110, 153)
        else:
            listOfMenuGroup[2].move(130, 153)

        # set titleLabelB if it exists
        if menuData[1][0] != False:
            listOfMenuGroup[2].setText(menuData[1][0])
            listOfMenuGroup[2].setFont(
                self.addFontWithPixel(10.5, 'Noto Sans KR', True))

        # load menuLabel
        menuText = ''
        for i in range(1, len(menuData[1])):
            menuText += menuData[1][i] + '\n'
        listOfMenuGroup[4].setText(menuText)
        listOfMenuGroup[4].setFont(
            self.addFontWithPixel(12, 'Noto Sans KR Medium'))

        # load priceLabel
        listOfMenuGroup[5].setText(menuData[2])
        listOfMenuGroup[5].setFont(
            self.addFontWithPixel(14))

    def loadmainGroup(self, tag):
        cnt = 0
        for reNum in range(3):
            # check tag
            for menu in self.reList[reNum]:
                if tag in menu[3]:
                    self.loadMenuGroup(
                        reNum, menu, self.lomg_tup[cnt]
                    )
                    cnt += 1
        return cnt

    # Initialize the widget and save it as a tuple in the instance attribute
    def initWidget(self):
        self.listOfMenuGroup1 = (self.MenuGroup_1, self.titleLabel_1A, self.titleLabel_1B,
                                 self.menuImage_1, self.menuLabel_1, self.priceLabel_1)
        self.listOfMenuGroup2 = (self.MenuGroup_2, self.titleLabel_2A, self.titleLabel_2B,
                                 self.menuImage_2, self.menuLabel_2, self.priceLabel_2)
        self.listOfMenuGroup3 = (self.MenuGroup_3, self.titleLabel_3A, self.titleLabel_3B,
                                 self.menuImage_3, self.menuLabel_3, self.priceLabel_3)
        self.listOfMenuGroup4 = (self.MenuGroup_4, self.titleLabel_4A, self.titleLabel_4B,
                                 self.menuImage_4, self.menuLabel_4, self.priceLabel_4)
        self.listOfMenuGroup5 = (self.MenuGroup_5, self.titleLabel_5A, self.titleLabel_5B,
                                 self.menuImage_5, self.menuLabel_5, self.priceLabel_5)
        self.listOfMenuGroup6 = (self.MenuGroup_6, self.titleLabel_6A, self.titleLabel_6B,
                                 self.menuImage_6, self.menuLabel_6, self.priceLabel_6)
        self.listOfMenuGroup7 = (self.MenuGroup_7, self.titleLabel_7A, self.titleLabel_7B,
                                 self.menuImage_7, self.menuLabel_7, self.priceLabel_7)
        self.listOfMenuGroup8 = (self.MenuGroup_8, self.titleLabel_8A, self.titleLabel_8B,
                                 self.menuImage_8, self.menuLabel_8, self.priceLabel_8)

        self.lomg_tup = (self.listOfMenuGroup1, self.listOfMenuGroup2, self.listOfMenuGroup3, self.listOfMenuGroup4,
                         self.listOfMenuGroup5, self.listOfMenuGroup6, self.listOfMenuGroup7, self.listOfMenuGroup8)

    def hideAll(self):
        for group in [self.MenuGroup_1, self.MenuGroup_2, self.MenuGroup_3, self.MenuGroup_4, self.MenuGroup_5, self.MenuGroup_6, self.MenuGroup_7, self.MenuGroup_8]:
            group.hide()
        self.refreshGif.hide()
        self.refreshLabel.hide()
