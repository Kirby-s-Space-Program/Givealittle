#App Configurations
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()

#Sizes
WIDTH_MAIN = screen.size().width()
HEIGHT_MAIN = screen.size().height()

LEFT_HEADER = int(WIDTH_MAIN/12)
TOP_HEADER = int(HEIGHT_MAIN/75)
WIDTH_HEADER = WIDTH_MAIN
HEIGHT_HEADER = int(HEIGHT_MAIN/10)
TOP_HEADER_SHADOW = int(TOP_HEADER + HEIGHT_HEADER/10)

LEFT_SEARCH = int(WIDTH_MAIN/5)
TOP_SEARCH = int(HEIGHT_MAIN/6)
WIDTH_SEARCH = int(3*WIDTH_MAIN/5)
HEIGHT_SEARCH = int(HEIGHT_MAIN/30)

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

#Color pallette
DARK_PINK = QColor(221, 4, 89) #"rgb(221, 4, 89)" #0xdd0459
PINK = QColor(235, 104, 150) #"rgb(235, 104, 150)" #0xeb6896
SOFT_PINK = QColor(253, 153, 167)   #"rgb(253, 153, 167)" #0xfd99a7
YELLOW = "rgb(251, 251, 143)" #0xfbfb8f
WHITE = 0xeeeeee
BLACK = 0x070a0d

#Images
SEARCH = "./icons/search.png"
HEADER_TITLE = "./icons/header_title.png"