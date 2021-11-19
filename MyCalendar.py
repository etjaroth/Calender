import StaticType
import main
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
    def __init__(self, QTGrid, x=1, y=1):
        self.calendar = calendar.Calendar()
        self.year = datetime.datetime.today().year
        self.month = datetime.datetime.today().month
        self.day = datetime.datetime.today().day

        self.QTGrid = StaticType.forceType(QTGrid, QGridLayout)
        self.x = StaticType.forceType(x, int)
        self.y = StaticType.forceType(y, int)

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

    def incrementMonth(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.displayToQTGrid()

    def decrementMonth(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.displayToQTGrid()

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

    def displayToQTGrid(self):
        # Year Header
        yearHeaderYOffset = 0
        calendarYear = QPushButton(str(self.year))
        calendarYear.setContentsMargins(0, 0, 0, 0)
        self.QTGrid.addWidget(calendarYear, self.y + yearHeaderYOffset, self.x, self.y + yearHeaderYOffset, self.x + 6)

        # Month Header
        monthHeaderYOffset = yearHeaderYOffset + 1
        calendarLeft = QPushButton("<")
        calendarLeft.setContentsMargins(0, 0, 0, 0)
        calendarLeft.clicked.connect(self.decrementMonth)
        self.QTGrid.addWidget(calendarLeft, self.y + monthHeaderYOffset, self.x)

        calendarRight = QPushButton(">")
        calendarRight.clicked.connect(self.incrementMonth)
        calendarRight.setContentsMargins(0, 0, 0, 0)
        self.QTGrid.addWidget(calendarRight, self.y + monthHeaderYOffset, self.x + 6)

        monthStr = ["January", "February", "March", "April", "May", "June", \
             "July", "August", "September", "October", "November", "December"]
        self.QTGrid.addWidget(QPushButton(monthStr[self.month - 1]), \
            self.y + monthHeaderYOffset, self.x + 1, self.y + monthHeaderYOffset, self.x + 4)

        # Weekday Header
        weekdayHeaderYOffset = monthHeaderYOffset + 5
        self.QTGrid.addWidget(QPushButton("Sunday"), self.y + weekdayHeaderYOffset, self.x + 0)
        self.QTGrid.addWidget(QPushButton("Monday"), self.y + weekdayHeaderYOffset, self.x + 1)
        self.QTGrid.addWidget(QPushButton("Tuesday"), self.y + weekdayHeaderYOffset, self.x + 2)
        self.QTGrid.addWidget(QPushButton("Wednesday"), self.y + weekdayHeaderYOffset, self.x + 3)
        self.QTGrid.addWidget(QPushButton("Thursday"), self.y + weekdayHeaderYOffset, self.x + 4)
        self.QTGrid.addWidget(QPushButton("Friday"), self.y + weekdayHeaderYOffset, self.x + 5)
        self.QTGrid.addWidget(QPushButton("Saturday"), self.y + weekdayHeaderYOffset, self.x + 6)

        # Calendar Body
        cX = self.x
        cXOrig = self.x
        cY = self.y + weekdayHeaderYOffset + 1
        i = 0
        c = calendar.Calendar()
        yearToday = datetime.datetime.today().year
        monthToday = datetime.datetime.today().month
        dayToday = datetime.datetime.today().day
        for day in c.itermonthdays(self.year, self.month):
            if day == 0:
                self.QTGrid.addWidget(QPushButton(" "), cY, cX)
            else:
                s = str(day)
                if day == 0:
                    s = ""

                button = QPushButton(s)
                button.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
                if day == dayToday and self.month == monthToday and self.year == yearToday:
                    button.setStyleSheet("background-color : yellow")
                self.QTGrid.addWidget(button, cY, cX)

            i += 1
            cX += 1
            if i == 7:
                cX = cXOrig
                cY += 1
                i = 0


if __name__ == '__main__':
    main.main()
