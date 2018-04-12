# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:00:56 2018

@author: LeeJiangLee
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
def addItem():
    if not dlg.lineEdit.text()=='':
        dlg.listWidget.addItem(dlg.lineEdit.text())
        dlg.lineEdit.setText("")
app = QtWidgets.QApplication([])
dlg = uic.loadUi('test.ui')
QMessageBox.information(None,"Title","Message")
dlg.pushButton.clicked.connect(addItem)
dlg.lineEdit.returnPressed.connect(addItem)
dlg.show()
app.exec()