#App Configurations
import sys
from tkinter import LEFT
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()

#Sizes
WIDTH_MAIN = screen.size().width()
HEIGHT_MAIN = screen.size().height()

HLAYOUT_HEIGHT = int(HEIGHT_MAIN/20)
HLAYOUT_WIDTH = int(WIDTH_MAIN/5)
HLAYOUT_LEFT = WIDTH_MAIN-HLAYOUT_WIDTH-100
HLAYOUT_TOP = 0
HLAYOUT_SPACING = 20

WIDTH_SUB = int(WIDTH_MAIN/4)
HEIGHT_SUB = int(HEIGHT_MAIN/2.5)
LEFT_SUB = int(WIDTH_MAIN/2 - WIDTH_SUB/2)
TOP_SUB = int(HEIGHT_MAIN/4)

MARGIN_SUB_VBOX = int(WIDTH_SUB/4)
TOP_SUB_VBOX = int(HEIGHT_SUB/10)

MARGIN_BUTTON = int(WIDTH_SUB/8)
