from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QObject, Signal, Slot  
from Infobar import InformationBar
import datetime
import sys
class ControlBar(QtWidgets.QWidget):
    advance_day = Signal()
    reduce_day = Signal()
    current_day = Signal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        #TODO can these buttons be styled better?
        self.prevButton = QtWidgets.QPushButton("Previous")
        self.nextButton = QtWidgets.QPushButton("Next")
        self.currentButton = QtWidgets.QPushButton("Current")
        ##assemble the controls
        self.layout.addWidget(self.prevButton)
        self.layout.addWidget(self.currentButton)
        self.layout.addWidget(self.nextButton)
        ## Wire up the signals
        self.prevButton.clicked.connect(self.previous_click)
        self.nextButton.clicked.connect(self.next_click)
        self.currentButton.clicked.connect(self.current_clicked)
        

    def previous_click(self):
        print("previous_clicked")
        self.reduce_day.emit()

    def next_click(self):
        print("next_clicked")
        self.advance_day.emit()
    def current_clicked(self):
        print("current_clicked")
        self.current_day.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ControlBar()
    widget.show()

    sys.exit(app.exec_())