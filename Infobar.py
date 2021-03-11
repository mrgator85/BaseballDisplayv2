from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QObject, Signal, Slot  
import datetime
import sys

class InformationBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.team_label = QtWidgets.QLabel("Reds", self)
       
        self.date_label = QtWidgets.QLabel("", self)
        ##Build the widget
        self.layout.addWidget(self.team_label)
        self.layout.setAlignment(self.team_label, QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.date_label)
        self.layout.setAlignment(self.date_label, QtCore.Qt.AlignRight)
        self.update_date(datetime.date.today())
    @Slot(datetime.date)
    def update_date(self, d):
        self.date_label.setText(d.strftime("%b %d %Y"))
    
    @Slot(str)
    def setTeam(self, team):
        self.team_label.setText(team)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = InformationBar()
    widget.show()

    sys.exit(app.exec_())