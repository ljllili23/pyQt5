# -*- coding: utf-8 -*-
"""
Created on 2018/4/20

@author: LeeJiangLee
"""
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication)
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal,self)
#         vbox = QVBoxLayout()
#         self.setLayout(vbox)
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         # self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Signal and Slot')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())