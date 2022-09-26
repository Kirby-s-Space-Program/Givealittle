from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *

class itemGrid(QWidget):
    def __init__(self, parentWindow): #parentWidnow is the mainWindow object to be passed as a parameter 
      super ().__init__()
      self.parentWindow = parentWindow


    def addGrid(self): 
      self.GridWidget = QWidget(self) #grid to contain vertical layouts
      self.GridWidget.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID, HEIGHT_GRID))
      self.GridWidget.setObjectName("GridWidget")
      self.GridWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.Grid = QGridLayout(self.GridWidget)
      self.Grid.setObjectName("Grid")
      self.roundCorners(10.0, self.GridWidget)

      self.vItemBox = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox.setObjectName("vItemBox")
      self.vItemBox.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.Grid.addLayout(self.vItemBox)

      self.vItemBox2 = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox2.setObjectName("vItemBox2")
      self.vItemBox2.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.setLayout(self.vItemBox2)

      self.vItemBox3 = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox3.setObjectName("vItemBox3")
      self.vItemBox3.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.setLayout(self.vItemBox3)

      self.vItemBox4 = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox4.setObjectName("vItemBox4")
      self.vItemBox4.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.setLayout(self.vItemBox4)

      self.vItemBox5 = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox5.setObjectName("vItemBox5")
      self.vItemBox5.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.setLayout(self.vItemBox5)

      self.vItemBox6 = QVBoxLayout(self.vGrid)  #vertical layout to store items
      self.vItemBox6.setObjectName("vItemBox6")
      self.vItemBox6.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX)
      self.setLayout(self.vItemBox6)
      
      self.imageBag = QPixmap("./product/bag.png")
      self.imageCycle = QPixmap("./product/cycle.png")
      self.imageFootball = QPixmap("./product/football.png")
      self.imageGlasses = QPixmap("./product/glasses.png")
      self.imageIphone = QPixmap("./product/iphone.png")
      self.imageIT = QPixmap("./product/IT.png")

      self.lblBag = QLabel(self)
      self.lblBag.setPixmap(self.imageBag)
      self.lblCycle = QLabel(self)
      self.lblCycle.setPixmap(self.imageCycle)
      self.lblFootball = QLabel(self)
      self.lblFootball.setPixmap(self.imageFootball)
      self.lblGlasses = QLabel(self)
      self.lblGlasses.setPixmap(self.imageGlasses)
      self.lblIphone = QLabel(self)
      self.lblIphone.setPixmap(self.imageIphone)
      self.lblIT = QLabel(self)
      self.lblIT.setPixmap(self.imageIT)

      self.vItemBox.addWidget(self.lblBag)
      self.vItemBox2.addWidget(self.lblCycle)
      self.vItemBox3.addWidget(self.lblFootball)
      self.vItemBox4.addWidget(self.lblGlasses)
      self.vItemBox5.addWidget(self.lblIphone)
      self.vItemBox6.addWidget(self.lblIT)