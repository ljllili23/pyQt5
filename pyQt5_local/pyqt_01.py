# -*- coding: utf-8 -*-
"""
Created on 2018/4/12

@author: LeeJiangLee
"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton,QApplication,QMessageBox,QDesktopWidget)
#from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        btn=QPushButton('Button',self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        #btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.center()
        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())