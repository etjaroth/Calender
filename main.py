import MyCalendar

# PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)

    layoutGrid = QGridLayout()
    layoutGrid.setHorizontalSpacing(0)
    layoutGrid.setVerticalSpacing(0)
    layoutGrid.setContentsMargins(0, 0, 0, 0)

    calendar = MyCalendar.MyCalendar(layoutGrid, 1, 1)
    calendar.displayToQTGrid()

    window = QWidget()
    window.setLayout(layoutGrid)
    window.setGeometry(100,100,200,100)

    window.setWindowTitle("Python Calendar")
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
