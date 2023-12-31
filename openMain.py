from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from ui_main import Ui_MainWindow
from fpd import fpdWindowApp


class mainWindowApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.connectButtons()
        self.fpds = []
        self.sims = []
        self.oprs = []

    def openFPD(self):
        self.fpds.append(fpdWindowApp())
        self.fpds[-1].show()

    def openSIM(self):
        1

    def openOPR(self):
        1

    def connectButtons(self):
        self.openFPDButton.clicked.connect(self.openFPD)
        self.openSIMButton.clicked.connect(self.openSIM)
        self.openOPRButton.clicked.connect(self.openOPR)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainWindowApp()
    win.show()
    app.exec()