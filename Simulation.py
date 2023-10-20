from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)
import sys
from ui_sim import Ui_SimWindow
from fpd import fpdWindowApp
from openMain import mainWindowApp


class simWindowApp(QMainWindow, Ui_SimWindow):
    def __init__(self, parent=None):
        super(simWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.connectButtons()
        self.fpds = []
        self.oprs = []
        self.main = []

    def openFPD(self):
        self.fpds.append(fpdWindowApp())
        self.fpds[-1].show()

    def openMain(self):
        self.main.append(mainWindowApp())
        self.main[-1].show()

    def connectButtons(self):
        self.BacktoMainButton.clicked.connect(self.openMain)
        self.EditFloorPlanButton.clicked.connect(self.openFPD)
        # self.SimulationButton.clicked.connect()
        # self.LoadFloorPlanButton.clicked.connect()
        # self.SimSpeedButton.clicked.connect()
        # self.VacuumLoadButton.clicked.connect()
        # self.VacuumSaveButton.clicked.connect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = simWindowApp()
    win.show()
    app.exec()