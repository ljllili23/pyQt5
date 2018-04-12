# -*- coding: utf-8 -*-
"""
Created on 2018/4/12

@author: LeeJiangLee
"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        btn=QPushButton('Button',self)
        btn.serToolTip("This is a <b>QPushButton</b> widget")
