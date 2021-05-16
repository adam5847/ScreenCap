from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PIL import ImageGrab
import time
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWidow")
        MainWindow.setFixedSize(408, 148)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setWindowTitle("ScreenCap")

        self.screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.screenshot.setGeometry(QtCore.QRect(10, 10, 91, 81))
        self.screenshot.setIcon(QIcon("icons/screen_icon.png"))
        self.screenshot.setIconSize(QSize(90,90))
        self.screenshot.setObjectName("screenshot")
        self.screenshot.clicked.connect(lambda: self.clicked_sceenshot())

        self.areascreenshot = QtWidgets.QPushButton(self.centralwidget)
        self.areascreenshot.setGeometry(QtCore.QRect(110, 10, 91, 81))
        self.areascreenshot.setIcon(QIcon("icons/areascreen_icon.png"))
        self.areascreenshot.setIconSize(QSize(90,90))
        self.areascreenshot.setObjectName("areascreenshot")

        self.careascreenshot = QtWidgets.QPushButton(self.centralwidget)
        self.careascreenshot.setGeometry(QtCore.QRect(210, 10, 91, 81))
        self.careascreenshot.setIcon(QIcon("icons/customareascreen_icon.png"))
        self.careascreenshot.setIconSize(QSize(90,90))
        self.careascreenshot.setObjectName("careascreenshot")

        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(310, 10, 91, 81))
        self.record.setIcon(QIcon("icons/record_icon.png"))
        self.record.setIconSize(QSize(90,90))
        self.record.setObjectName("record")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 26))
        self.menubar.setObjectName("menubar")

        self.menuScreenshot = QtWidgets.QMenu(self.menubar)
        self.menuScreenshot.setObjectName("menuScreenshot")

        self.menuScreen_record = QtWidgets.QMenu(self.menubar)
        self.menuScreen_record.setObjectName("menuScreen_record")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionDirectory = QtWidgets.QAction(MainWindow)
        self.actionDirectory.setObjectName("actionDirectory")

        self.actionFormat = QtWidgets.QAction(MainWindow)
        self.actionFormat.setObjectName("actionFormat")

        self.actionDirectory_video = QtWidgets.QAction(MainWindow)
        self.actionDirectory_video.setObjectName("actionDirectory_video")

        self.actionFormat_video = QtWidgets.QAction(MainWindow)
        self.actionFormat_video.setObjectName("actionFormat_video")

        self.menuScreenshot.addAction(self.actionDirectory)
        self.menuScreenshot.addAction(self.actionFormat)

        self.menuScreen_record.addAction(self.actionDirectory_video)
        self.menuScreen_record.addAction(self.actionFormat_video)

        self.menubar.addAction(self.menuScreenshot.menuAction())
        self.menubar.addAction(self.menuScreen_record.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionDirectory.triggered.connect(lambda: self.clicked_folder())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuScreenshot.setTitle(_translate("MainWindow", "Screenshot"))
        self.menuScreen_record.setTitle(_translate("MainWindow", "Screen record"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionDirectory.setText(_translate("MainWindow", "Directory"))
        self.actionFormat.setText(_translate("MainWindow", "Format"))
        self.actionDirectory_video.setText(_translate("MainWindow", "Directory"))
        self.actionFormat_video.setText(_translate("MainWindow", "Format"))

    def clicked_folder(self):
        self.screenshot_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder','C:/Users')
        f = open('memory_screenshot.txt','r')
        lst = f.read().split(',')
        f.close()
        f = open('memory_screenshot.txt','w')
        lst[2] = self.screenshot_path
        f.write('{0},{1},{2}'.format(lst[0],lst[1],lst[2]))
        f.close()

    def clicked_sceenshot(self):
        f = open('memory_screenshot.txt','r')
        lst = f.read().split(',')
        i = int(lst[0])+1
        i = str(i)
        path  = lst[2] + '/screenshot' + i + '.' + lst[1]
        f.close()
        MainWindow.showMinimized()
        time.sleep(0.5)
        screenshot = ImageGrab.grab()
        screenshot.save(path, lst[1])
        MainWindow.showNormal()
        f = open('memory_screenshot.txt','w')
        f.write('{0},{1},{2}'.format(i,lst[1],lst[2]))
        f.close()

if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
