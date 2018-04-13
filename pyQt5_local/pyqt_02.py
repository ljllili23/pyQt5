# -*- coding: utf-8 -*-
"""
Created on 2018/4/12

@author: LeeJiangLee
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('ready')
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
