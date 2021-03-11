from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QObject, Signal, Slot  
from Infobar import InformationBar
from ControlBar import ControlBar
import sys
import datetime

class LiveGame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.linescore_label = QtWidgets.QLabel("Game Data",self)
        self.linescore_label.setWordWrap(True)
        self.linescore_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.linescore_label.setStyleSheet("border: 1px solid black")
        #To eventually hold the "Pitching: name Batting: name"
        self.state_label = QtWidgets.QLabel("pitching", self)
        self.layout.addWidget(self.linescore_label)
        self.layout.addWidget(self.state_label)

    @Slot(str)
    def UpdateLine(self, line):
        self.linescore_label.setText(line)

    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = LiveGame()
    #widget.resize(480, 320)
    widget.show()

    sys.exit(app.exec_())