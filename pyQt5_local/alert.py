# -*- coding: utf-8 -*-
"""
Created on 2018/4/12

@author: LeeJiangLee
"""
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv)<2:
        raise ValueError
    hours,mins=sys.argv[1].split(":")
    due = QTime(int(hours),int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv)>2:
        message = " ".join(sys.argv[2:])   # str.join(sequence)
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" #24hr clock

while QTime.currentTime()<due:
    time.sleep(20)

label = QLabel("<font color=red size=72><b>"+message+"</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(2000,app.quit)
app.exec_()
