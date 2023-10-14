from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from ui_fpd import Ui_FPDWindow

class fpdWindowApp(QMainWindow, Ui_FPDWindow):
    def __init__(self, parent=None):
        super(fpdWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.connectButtons()


    def connectButtons(self):
        1
