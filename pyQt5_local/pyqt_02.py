# -*- coding: utf-8 -*-
"""
Created on 2018/4/12

@author: LeeJiangLee
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp,QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # def initUI(self):
    #
    #     exitAct = QAction(QIcon('exit.png'),'&Exit',self)
    #     exitAct.setShortcut('Ctrl+Q')
    #     exitAct.setStatusTip('Exit Application')
    #     exitAct.triggered.connect(qApp.quit)
    #     self.statusBar()
    #     menubar = self.menuBar()
    #     fileMenu = menubar.addMenu('File')
    #     fileMenu.addAction(exitAct)
    #     impMenu = QMenu('Import',self)  # create File's Import submenu with QMenu()
    #     impAct = QAction('Import mail',self)
    #     impMenu.addAction(impAct)   # An action is added to the submenu with addAction()
    #     newAct = QAction('New',self)
    #     fileMenu.addAction(newAct)
    #     fileMenu.addMenu(impMenu)
    #
    #     viewMenu = menubar.addMenu('View')
    #     viewStatAct = QAction('view statusbar',self,checkable=True)
    #     viewStatAct.setStatusTip('view statusbar')
    #     viewStatAct.setChecked(True)
    #     viewStatAct.triggered.connect(self.toggleMenu)
    #     viewMenu.addAction(viewStatAct)
    #
    #
    #
    #     self.setGeometry(300,300,300,200)
    #     self.setWindowTitle('Check menu')
    #     self.show()
    # def toggleMenu(self,state):
    #     if state:
    #         self.statusBar.show()
    #     else:
    #         self.statusBar.hide()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = QMenu('View',self,)
        viewMenu.setStatusTip('View')
        menubar.addMenu(viewMenu)



        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
