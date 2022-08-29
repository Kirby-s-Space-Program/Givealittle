#App Configurations
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()

#Sizes
SIZE_WIDTH_MAIN = screen.size().width()
SIZE_HEIGHT_MAIN = screen.size().height()

HLAYOUT_HEIGHT = int(SIZE_HEIGHT_MAIN/20)
HLAYOUT_WIDTH = int(SIZE_WIDTH_MAIN/5)
HLAYOUT_LEFT = SIZE_WIDTH_MAIN-HLAYOUT_WIDTH-100
HLAYOUT_TOP = 0
HLAYOUT_SPACING = 20