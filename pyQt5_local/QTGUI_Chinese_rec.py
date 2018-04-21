# -*- coding: utf-8 -*-
"""
Created on 2018/4/20

@author: LeeJiangLee
"""
from PyQt5.QtWidgets import (QMainWindow,QLineEdit,QAction,QFileDialog,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,)
from PyQt5.QtGui import QIcon,QPixmap,QFont
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.myFileStr = '../data/test/00999/223400.png'    # 这是inference的输入
        self.ans='帆'        # 这是inference的结果
    def initUI(self):
        LineEdit = QLineEdit(self.myFileStr)
        okButton = QPushButton("OK")
        openButton = QPushButton("...")
        pixmap = QPixmap(self.myFileStr)
        ansLabel = QLabel(self.ans)
        ansLabel.setFont(QFont("ZhongSong",23,QFont.Bold))

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(LineEdit)
        hbox_1.addWidget(openButton)
        hbox_1.addstretch(1)
        hbox_1.addWidget(okButton)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(pixmap)
        hbox_2.addStretch(1)
        hbox_2.addWidget(ansLabel)


        vbox = QVBoxLayout()
        vbox.addWidget(hbox_1)
        vbox.addWidget()