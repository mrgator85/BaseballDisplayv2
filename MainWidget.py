from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QObject, Signal, Slot  
from Infobar import InformationBar
from ControlBar import ControlBar
from BaseballData import BaseballData
from LiveGame import LiveGame
import sys
import datetime
class MainWidget(QtWidgets.QWidget):
    """This is the main widget of the baseball display.
    Will feature an information bar (Layout)on the top (date, team, etc)
    A Stacked layout in the main area to allow for swapping out differnent
    display widgets
    A control layout on the bottom with buttons for next, prev, current, etc
    """
    def __init__(self):
        super(MainWidget, self).__init__()
        #QT Stuff
        self.resize(480, 320)
        self.vLayout = QtWidgets.QVBoxLayout(self)
        self.info_bar = InformationBar()
        self.info_bar.setStyleSheet("border: 1px solid green")
        self.stackLayout = QtWidgets.QStackedWidget()
        self.stackLayout.setStyleSheet("border: 1px solid blue")
        
        self.control_bar = ControlBar()
        self.control_bar.setStyleSheet("border: 1px solid red")
        self.vLayout.addWidget(self.info_bar)
        self.vLayout.addWidget(self.stackLayout)
        self.vLayout.addWidget(self.control_bar)
        self.gamedisplay = LiveGame()
        self.gamedisplay.setStyleSheet("border: 1px solid black")
        self.stackLayout.addWidget(self.gamedisplay)
        ## Game state stuff
        self.baseball = BaseballData()
        self.currentDate = datetime.datetime.now()
        self.selectedDate = self.currentDate
        self.teamid = 113
        ##connect to controls
        self.control_bar.advance_day.connect(self.advance_day)
        self.control_bar.reduce_day.connect(self.previous_day)
        self.control_bar.current_day.connect(self.current_day)


    @Slot()
    def advance_day(self):
        self.selectedDate += datetime.timedelta(days=1)
        self.update()
    
    @Slot()
    def previous_day(self):
        self.selectedDate -= datetime.timedelta(days=1)
        self.update()

    @Slot()
    def current_day(self):
        self.selectedDate = self.currentDate
        self.update()

    def update(self):
        self.info_bar.update_date(self.selectedDate)
        gameid = self.baseball.get_game_id_from_date(self.getDateString(self.selectedDate), self.teamid)
        if(gameid > 0):
            linescore = self.baseball.get_linescore(gameid)
        else:
            linescore = "No game on selected day"
        self.gamedisplay.UpdateLine(linescore)
        
    def getDateString(self, date):
        return date.strftime("%m/%d/%Y")
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.show()

    sys.exit(app.exec_())