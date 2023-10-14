from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from ui_fpd import Ui_FPDWindow

class fpdWindowApp(QMainWindow, Ui_FPDWindow):
    def __init__(self, parent=None):
        super(fpdWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.connectButtons()
        self.numRooms = 1
        self.rooms = []
        self.room1.setObjectName("Room 1")
        self.rooms.append(self.room1)


    def saveFloorplan(self):
        _translate = QtCore.QCoreApplication.translate
        self.saveFloorplanButton.setText(_translate("MainWindow", "Floorplan Saved!"))

    def loadFloorplan(self):
        1

    def newFloorplan(self):
        1

    def addRoom(self):
        newRoomText = self.textEdit.toPlainText()
        for i in range(0, self.numRooms):
            if self.rooms[i].objectName() == newRoomText or newRoomText == '':
                return
        self.floorplanView.setCurrentIndex(1)
        self.r3 = QtWidgets.QFrame(self.overviewTab)
        self.r3.setGeometry(QtCore.QRect(100, 100, 301, 181))
        font = QtGui.QFont()
        font.setKerning(True)
        self.r3.setFont(font)
        self.r3.setFrameShape(QtWidgets.QFrame.Box)
        self.r3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.r3.setLineWidth(1)
        self.r3.setObjectName(newRoomText)
        self.floorplanView.setCurrentIndex(0)

        self.room = QtWidgets.QWidget()
        self.room.setObjectName(newRoomText)
        self.roomFull = QtWidgets.QFrame(self.room)
        self.roomFull.setGeometry(QtCore.QRect(20, 20, 600, 480))
        font = QtGui.QFont()
        font.setKerning(True)
        self.roomFull.setFont(font)
        self.roomFull.setFrameShape(QtWidgets.QFrame.Box)
        self.roomFull.setFrameShadow(QtWidgets.QFrame.Plain)
        self.roomFull.setLineWidth(1)
        self.roomFull.setObjectName(newRoomText + "_full")
        self.floorplanView.addTab(self.room, newRoomText)
        self.rooms.append(self.room)
        

    def connectButtons(self):
        self.addRoomButton.clicked.connect(self.addRoom)
        self.saveFloorplanButton.clicked.connect(self.saveFloorplan)
