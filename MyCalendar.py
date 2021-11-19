import StaticType
import calendar
import datetime

# To clear terminal
import os

# Colored terminal text
from colorama import Fore
from colorama import Style

# Graphics Display
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyCalendar():
    def __init__(self):
        self.calendar = calendar.Calendar()
        self.year = datetime.datetime.today().year
        self.month = datetime.datetime.today().month
        self.day = datetime.datetime.today().day

    def getYear(self):
        return StaticType.forceType(self.year, int)

    def setYear(self, year):
        self.year = StaticType.forceType(year, int)

    def getMonth(self):
        return StaticType.forceType(self.month, int)

    def setMonth(self, month):
        self.month = StaticType.forceType(month, int)

    def getDay(self):
        return StaticType.forceType(self.day, int)

    def setDay(self, day):
        self.day = StaticType.forceType(day, int)

    def displayText(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        i = 0
        c = calendar.Calendar()

        #print(calendar.month(self.year, self.month))
        # print("--------------------")

        print("Mo Tu We Th Fr Sa Su")
        for day in c.itermonthdays(self.year, self.month):
            if day < 10:
                print(" ", end='')

            if day == 0:
                print("  ", end='')
            else:
                if day == self.day:
                    print(f"{Fore.YELLOW}", end='')
                print(day, end=f" {Style.RESET_ALL}")

            i += 1
            if i == 7:
                print()
                i = 0

    def displayToQTGrid(self, QTGrid, x=0, y=0):
        StaticType.forceType(QTGrid, QGridLayout)
        StaticType.forceType(x, int)
        StaticType.forceType(y, int)

        QTGrid.addWidget(QPushButton("Sunday"), y, x + 0)
        QTGrid.addWidget(QPushButton("Monday"), y, x + 1)
        QTGrid.addWidget(QPushButton("Tuesday"), y, x + 2)
        QTGrid.addWidget(QPushButton("Wednesday"), y, x + 3)
        QTGrid.addWidget(QPushButton("Thursday"), y, x + 4)
        QTGrid.addWidget(QPushButton("Friday"), y, x + 5)
        QTGrid.addWidget(QPushButton("Saturday"), y, x + 6)

        cX = x
        cXOrig = x
        cY = y + 1
        i = 0
        c = calendar.Calendar()
        for day in c.itermonthdays(self.year, self.month):
            if day == 0:
                QTGrid.addWidget(QPushButton(" "), cY, cX)
            else:
                s = str(day)
                if day == 0:
                    s = ""

                button = QPushButton(s)
                if day == self.day:
                    button.setStyleSheet("background-color : yellow")
                QTGrid.addWidget(button, cY, cX)

            i += 1
            cX += 1
            if i == 7:
                cX = cXOrig
                cY += 1
                i = 0

if __name__ == '__main__':
    c = MyCalendar()
    c.displayText()
