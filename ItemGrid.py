from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *

class itemGrid(QWidget):
    def __init__(self, parentWindow): #parentWidnow is the mainWindow object to be passed as a parameter 
      super ().__init__()
      self.parentWindow = parentWindow
      self.addGrid()


    def addGrid(self): 
      self.GridWidget = QWidget(self.parentWindow) #grid to contain vertical layouts
      self.GridWidget.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID, HEIGHT_GRID))
      self.GridWidget.setObjectName("GridWidget")
      self.GridWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.Grid = QGridLayout(self.GridWidget)
      self.Grid.setObjectName("Grid")
      self.parentWindow.roundCorners(10.0, self.GridWidget)

      self.vItemBoxWidget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBoxWidget.setObjectName("vItemBoxWidget")
      self.vItemBoxWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBox = QVBoxLayout(self.vItemBoxWidget)  #vertical layout to store items
      self.vItemBox.setObjectName("vItemBox")
      self.Grid.addWidget(self.vItemBoxWidget, 0, 0)
      
      self.vItemBo2xWidget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBo2xWidget.setObjectName("vItemBo2xWidget")
      self.vItemBo2xWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBo2xWidget.setContentsMargins(20, 0,0,0)
      self.vItemBox2 = QVBoxLayout(self.vItemBo2xWidget)  #vertical layout to store items
      self.vItemBox2.setObjectName("vItemBox2")
      self.Grid.addWidget(self.vItemBo2xWidget, 0, 1)

      self.vItemBo3xWidget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBo3xWidget.setObjectName("vItemBo3xWidget")
      self.vItemBo3xWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBox3 = QVBoxLayout(self.vItemBo3xWidget)  #vertical layout to store items
      self.vItemBox3.setObjectName("vItemBox3")
      self.Grid.addWidget(self.vItemBo3xWidget, 0, 2)

      self.vItemBo4xWidget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBo4xWidget.setObjectName("vItemBo4xWidget")
      self.vItemBo4xWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBox4 = QVBoxLayout(self.vItemBo4xWidget)  #vertical layout to store items
      self.vItemBox4.setObjectName("vItemBox4")
      self.Grid.addWidget(self.vItemBo4xWidget, 1, 0)

      self.vItemBox5Widget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBox5Widget.setObjectName("vItemBox5Widget")
      self.vItemBox5Widget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBox5 = QVBoxLayout(self.vItemBox5Widget)  #vertical layout to store items
      self.vItemBox5.setObjectName("vItemBox5")
      self.Grid.addWidget(self.vItemBox5Widget, 1, 1)

      self.vItemBox6Widget = QWidget(self.GridWidget) #grid to contain vertical layouts
      self.vItemBox6Widget.setObjectName("vItemBox6Widget")
      self.vItemBox6Widget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vItemBox6 = QVBoxLayout(self.vItemBox6Widget)  #vertical layout to store items
      self.vItemBox6.setObjectName("vItemBox6")
      self.vItemBox6Widget.setContentsMargins(70, 0,0,0)
      self.Grid.addWidget(self.vItemBox6Widget, 1, 2)
      
      self.imageBag = QPixmap("./product/bag2.png")
      self.imageCycle = QPixmap("./product/cycle2.png")
      self.imageFootball = QPixmap("./product/football2.png")
      self.imageGlasses = QPixmap("./product/glasses2.png")
      self.imageIphone = QPixmap("./product/iphone2.png")
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


      #wishlist and carts
      self.hWishLayoutWidget = QWidget(self)
      self.hWishLayoutWidget.setObjectName("hWishLayoutWidget")
      self.hWishLayoutWidget.setContentsMargins(80, 0,0,0)
      self.hWishLayout = QHBoxLayout(self.hWishLayoutWidget)
      self.hWishLayout.setObjectName("hWishLayout")
      self.vItemBox.addWidget(self.hWishLayoutWidget)
      
      self.hWishLayoutWidget1 = QWidget(self)
      self.hWishLayoutWidget1.setObjectName("hWishLayoutWidget1")
      self.hWishLayoutWidget1.setContentsMargins(50, 0,0,0)
      self.hWishLayout1 = QHBoxLayout(self.hWishLayoutWidget1)
      self.hWishLayout1.setObjectName("hWishLayout1")
      self.vItemBox2.addWidget(self.hWishLayoutWidget1)

      self.hWishLayoutWidget2 = QWidget(self)
      self.hWishLayoutWidget2.setObjectName("hWishLayoutWidget2")
      self.hWishLayoutWidget2.setContentsMargins(80, 0,0,0)
      self.hWishLayout2 = QHBoxLayout(self.hWishLayoutWidget2)
      self.hWishLayout2.setObjectName("hWishLayout2")
      self.vItemBox3.addWidget(self.hWishLayoutWidget2)

      self.hWishLayoutWidget3 = QWidget(self)
      self.hWishLayoutWidget3.setObjectName("hWishLayoutWidget3")
      self.hWishLayoutWidget3.setContentsMargins(80, 0,0,0)
      self.hWishLayout3 = QHBoxLayout(self.hWishLayoutWidget3)
      self.hWishLayout3.setObjectName("hWishLayout3")
      self.vItemBox4.addWidget(self.hWishLayoutWidget3)

      self.hWishLayoutWidget4 = QWidget(self)
      self.hWishLayoutWidget4.setObjectName("hWishLayoutWidget4")
      self.hWishLayoutWidget4.setContentsMargins(60, 0,0,0)
      self.hWishLayout4 = QHBoxLayout(self.hWishLayoutWidget4)
      self.hWishLayout4.setObjectName("hWishLayout")
      self.vItemBox5.addWidget(self.hWishLayoutWidget4)

      self.hWishLayoutWidget5 = QWidget(self)
      self.hWishLayoutWidget5.setObjectName("hWishLayoutWidget5")
      self.hWishLayoutWidget5.setContentsMargins(15, 0,0,0)
      self.hWishLayout5 = QHBoxLayout(self.hWishLayoutWidget5)
      self.hWishLayout5.setObjectName("hWishLayout5")
      self.vItemBox6.addWidget(self.hWishLayoutWidget5)
      #----------------------------------------------------

      self.lblCart = QLabel(self.hWishLayoutWidget)
      self.lblCart.setPixmap(QPixmap(CART))
      self.lblWish = QLabel(self.hWishLayoutWidget)
      self.lblWish.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout.addWidget(self.lblWish)
      self.hWishLayout.addWidget(self.lblCart)

      self.lblCart1 = QLabel(self.hWishLayoutWidget1)
      self.lblCart1.setPixmap(QPixmap(CART))
      self.lblWish1 = QLabel(self.hWishLayoutWidget1)
      self.lblWish1.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout1.addWidget(self.lblWish1)
      self.hWishLayout1.addWidget(self.lblCart1)

      self.lblCart2 = QLabel(self.hWishLayoutWidget2)
      self.lblCart2.setPixmap(QPixmap(CART))
      self.lblWish2 = QLabel(self.hWishLayoutWidget2)
      self.lblWish2.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout2.addWidget(self.lblWish2)
      self.hWishLayout2.addWidget(self.lblCart2)

      self.lblCart3 = QLabel(self.hWishLayoutWidget3)
      self.lblCart3.setPixmap(QPixmap(CART))
      self.lblWish3 = QLabel(self.hWishLayoutWidget3)
      self.lblWish3.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout3.addWidget(self.lblWish3)
      self.hWishLayout3.addWidget(self.lblCart3)

      self.lblCart4 = QLabel(self.hWishLayoutWidget4)
      self.lblCart4.setPixmap(QPixmap(CART))
      self.lblWish4 = QLabel(self.hWishLayoutWidget4)
      self.lblWish4.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout4.addWidget(self.lblWish4)
      self.hWishLayout4.addWidget(self.lblCart4)

      self.lblCart5 = QLabel(self.hWishLayoutWidget5)
      self.lblCart5.setPixmap(QPixmap(CART))
      self.lblWish5 = QLabel(self.hWishLayoutWidget5)
      self.lblWish5.setPixmap(QPixmap(WISHLIST))
      self.hWishLayout5.addWidget(self.lblWish5)
      self.hWishLayout5.addWidget(self.lblCart5)

    def addNewItem(self):  #TODO: make the funciton with item input
      print("I WAS HDING")