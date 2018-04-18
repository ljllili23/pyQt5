# -*- coding: utf-8 -*-
"""
Created on 2018/4/17

@author: LeeJiangLee
"""

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QGridLayout,QPushButton,QMainWindow,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Bck','','close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)
            self.move(300,150)
            self.setWindowTitle('Calculator')
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
