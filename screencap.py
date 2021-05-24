# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screencap.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PIL import ImageGrab
import time
from os import environ 
import os.path
import json
from datetime import datetime

config = {
  "image": {
    "name": "screenshot",
    "extension": ".png",
    "path": None
  },
  "video": {
    "name": "screenrecord",
    "extension": ".mp4",
    "path": None
  }
}

def qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def clicked_format(extension):
    if config['image']['extension'] != extension:
        config['image']['extension'] = extension
        save_config()

def clicked_folder():
    screenshot_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder', config['image']['path'])
    if screenshot_path:
        if config['image']['path'] != screenshot_path:
            config['image']['path'] = screenshot_path
            save_config()

def save_config():
    with open('memory.json', 'w') as f:
        json.dump(config, f, indent=2)

def screenshot_path():
    if (config['image']['path']) is None:
        clicked_folder()
    if config['image']['path']:
        now = datetime.now()
        timeNow = now.strftime("%d-%m-%Y %H.%M.%S")
        path = os.path.join(config['image']['path'], config['image']['name'] + timeNow + config['image']["extension"])
        return path

def showDialog():
    msgWindow = QMessageBox()
    msgWindow.setIcon(QMessageBox.Information)
    msgWindow.setText("Screenshot is saved in " + config['image']['path'])
    msgWindow.setWindowTitle("ScreenCap")  
    msgWindow.exec_()
    msgWindow.showNormal()

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setFixedSize(409, 126)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.screenshot.setGeometry(QtCore.QRect(10, 10, 91, 81))
        self.screenshot.setText("")
        self.screenshot.setIcon(QIcon("icons/screen_icon.png"))
        self.screenshot.setIconSize(QSize(90,90))
        self.screenshot.setObjectName("screenshot")
        self.screenshot.clicked.connect(lambda: self.clicked_sceenshot())
        self.areascreenshot = QtWidgets.QPushButton(self.centralwidget)
        self.areascreenshot.setGeometry(QtCore.QRect(110, 10, 91, 81))
        self.areascreenshot.setText("")
        self.areascreenshot.setIcon(QIcon("icons/areascreen_icon.png"))
        self.areascreenshot.setIconSize(QSize(90,90))
        self.areascreenshot.setObjectName("areascreenshot")
        self.areascreenshot.clicked.connect(lambda: self.clicked_areasceenshot())
        self.careascreenshot = QtWidgets.QPushButton(self.centralwidget)
        self.careascreenshot.setGeometry(QtCore.QRect(210, 10, 91, 81))
        self.careascreenshot.setText("")
        self.careascreenshot.setIcon(QIcon("icons/customareascreen_icon.png"))
        self.careascreenshot.setIconSize(QSize(90,90))
        self.careascreenshot.setObjectName("careascreenshot")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(310, 10, 91, 81))
        self.record.setText("")
        self.record.setIcon(QIcon("icons/record_icon.png"))
        self.record.setIconSize(QSize(90,90))
        self.record.setObjectName("record")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 26))
        self.menubar.setObjectName("menubar")
        self.menuScreenshot = QtWidgets.QMenu(self.menubar)
        self.menuScreenshot.setObjectName("menuScreenshot")
        self.menuFormat = QtWidgets.QMenu(self.menuScreenshot)
        self.menuFormat.setObjectName("menuFormat")
        self.menuScreen_record = QtWidgets.QMenu(self.menubar)
        self.menuScreen_record.setObjectName("menuScreen_record")
        self.menuFormat_2 = QtWidgets.QMenu(self.menuScreen_record)
        self.menuFormat_2.setObjectName("menuFormat_2")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        mainWindow.setMenuBar(self.menubar)
        self.actionFolder = QtWidgets.QAction(mainWindow)
        self.actionFolder.setObjectName("actionFolder")
        self.actionjpg = QtWidgets.QAction(mainWindow)
        self.actionjpg.setObjectName("actionjpg")
        self.actionpng = QtWidgets.QAction(mainWindow)
        self.actionpng.setObjectName("actionpng")
        self.actionFolder_2 = QtWidgets.QAction(mainWindow)
        self.actionFolder_2.setObjectName("actionFolder_2")
        self.actionmp4 = QtWidgets.QAction(mainWindow)
        self.actionmp4.setObjectName("actionmp4")
        self.actionavi = QtWidgets.QAction(mainWindow)
        self.actionavi.setObjectName("actionavi")
        self.actionmvk = QtWidgets.QAction(mainWindow)
        self.actionmvk.setObjectName("actionmvk")
        self.menuFormat.addAction(self.actionjpg)
        self.menuFormat.addAction(self.actionpng)
        self.menuScreenshot.addAction(self.actionFolder)
        self.menuScreenshot.addAction(self.menuFormat.menuAction())
        self.menuFormat_2.addAction(self.actionmp4)
        self.menuFormat_2.addAction(self.actionavi)
        self.menuFormat_2.addAction(self.actionmvk)
        self.menuScreen_record.addAction(self.actionFolder_2)
        self.menuScreen_record.addAction(self.menuFormat_2.menuAction())
        self.menubar.addAction(self.menuScreenshot.menuAction())
        self.menubar.addAction(self.menuScreen_record.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.actionFolder.triggered.connect(lambda: clicked_folder())
        self.actionjpg.triggered.connect(lambda: clicked_format(".jpg"))
        self.actionpng.triggered.connect(lambda: clicked_format(".png"))
 
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ScreenCap"))
        self.menuScreenshot.setTitle(_translate("mainWindow", "Screenshot"))
        self.menuFormat.setTitle(_translate("mainWindow", "Format"))
        self.menuScreen_record.setTitle(_translate("mainWindow", "Screen record"))
        self.menuFormat_2.setTitle(_translate("mainWindow", "Format"))
        self.menuAbout.setTitle(_translate("mainWindow", "About"))
        self.actionFolder.setText(_translate("mainWindow", "Folder"))
        self.actionjpg.setText(_translate("mainWindow", "jpg"))
        self.actionpng.setText(_translate("mainWindow", "png"))
        self.actionFolder_2.setText(_translate("mainWindow", "Folder"))
        self.actionmp4.setText(_translate("mainWindow", "mp4"))
        self.actionavi.setText(_translate("mainWindow", "avi"))
        self.actionmvk.setText(_translate("mainWindow", "mvk"))
            
    def clicked_sceenshot(self):
        mainWindow.close()
        time.sleep(0.5)
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path())
        showDialog()
        mainWindow.showNormal()

    def clicked_areasceenshot(self):
        mainWindow.close()
        self.window = AreaScreenshot()
        mainWindow.showMinimized()

class AreaScreenshot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        screen = app.desktop().screenGeometry()
        width, height = screen.width(), screen.height()
        self.setGeometry(0, 0, width, height)
        self.setWindowOpacity(0.2)
        self.start = QtCore.QPoint()
        self.end = QtCore.QPoint()
        _translate = QtCore.QCoreApplication.translate
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowTitle(_translate("self", "ScreenCap")) 
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        paint = QtGui.QPainter(self)
        paint.setPen(QtGui.QPen(QtGui.QColor('blue'),2))
        paint.setBrush(QtGui.QColor(126, 191, 255, 128))
        paint.drawRect(QtCore.QRect(self.start, self.end))

    def mousePressEvent(self, event):
        self.start = event.pos()
        self.end = self.start
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        a = min(self.start.x(), self.end.x())
        b = min(self.start.y(), self.end.y())
        c = max(self.start.x(), self.end.x())
        d = max(self.start.y(), self.end.y())
        self.setWindowOpacity(0)
        areascreenshot = ImageGrab.grab(bbox=(a, b , c, d))
        areascreenshot.save(screenshot_path())
        time.sleep(0.5)
        showDialog()
        mainWindow.showNormal()
        self.close()

if __name__ == "__main__":
    qt_warnings()
    if (os.path.exists("memory.json")):
        with open('memory.json', 'r') as f:
            config = json.load(f)   
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())