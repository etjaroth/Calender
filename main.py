import MyCalendar

# PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)

    layoutGrid = QGridLayout()
    calendar = MyCalendar.MyCalendar()
    calendar.displayToQTGrid(layoutGrid, 1, 1)

    window = QWidget()
    window.setLayout(layoutGrid)
    window.setGeometry(100,100,200,100)

    window.setWindowTitle("Python Calendar")
    window.show()


    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
