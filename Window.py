from ast import BoolOp
from re import S
import sys
from turtle import color
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *
from database import register, login
from user import *
from login.encrypter import encrypt
from login.verification import *
from ItemGrid import *

logged = 2 #-1=external error, 0=logged in, 1=wrong details, 2=have not tried
user=currUser()

#-------------------------------------------------------------------------------------Base Class Window
class Window(QWidget):  
   def __init__(self):
      super ().__init__()

      self.title = "Kirby's Marketplace" #define window attributes
      self.left = LEFT_SUB
      self.top = TOP_SUB
      self.width = WIDTH_SUB
      self.height = HEIGHT_SUB
      self.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")

      self.vbox = QVBoxLayout()
      self.vbox.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX) 
      self.setLayout(self.vbox)

      self.InitUI()

   def InitUI(self) :  #set window attributes
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self. width, self.height)
      self.setWindowIcon(QIcon("logo.png"))

   def roundCorners(self, radius, widget): #round the corners    
      path = QPainterPath()
      path.addRoundedRect(QRectF(widget.rect()), radius, radius)
      mask = QRegion(path.toFillPolygon().toPolygon())
      widget.setMask(mask)

#-----------------------------------------------------------------------------------------Subclass MainWindow
class MainWindow(Window): 
   def __init__(self):
      super().__init__()

      self.width = WIDTH_MAIN
      self.height = HEIGHT_MAIN
      
      self.logged = 1 #0=logged in, 1=not logged in
      self.menubar = QMenuBar(self)
      self.menubar.setGeometry(QRect(0, 0, 1116, 21))
      self.menubar.setObjectName("menubar")

      self.InitUI()
      self.addMenu()
      self.addHeader()
      self.addSearch()
      self.addItemGrid()
      self.addDepartments()

   def addDepartments(self):
      self.vDepBoxWidget = QWidget(self)
      self.vDepBoxWidget.setGeometry(QRect(LEFT_DEP, TOP_DEP, WIDTH_DEP, HEIGHT_DEP))
      self.vDepBoxWidget.setObjectName("vDepBoxWidget")
      self.vDepBoxWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vDepBox = QVBoxLayout(self.vDepBoxWidget)
      self.vDepBox.setObjectName("vItemBox")
      self.roundCorners(10.0, self.vDepBoxWidget)

      #Header title
      self.lblDepartments = QLabel(self.vDepBoxWidget)
      self.lblDepartments.setText("Departments")
      self.lblDepartments.setGeometry(QRect(10, 0, WIDTH_DEP-30, 60))
      self.lblDepartments.setFont(QFont('AnyStyle', 30))
      self.lblDepartments.setStyleSheet("color : rgb(" + str(YELLOW.red()) + "," + str(YELLOW.green()) + "," + str(YELLOW.blue()) + ");")
      self.vDepBox.addWidget(self.lblDepartments)
      
      #Sport
      self.hSportLayoutWidget = QWidget(self)
      self.hSportLayoutWidget.setObjectName("hSportLayoutWidget")
      self.hSportLayoutWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.hSportLayout = QHBoxLayout(self.hSportLayoutWidget)
      self.hSportLayout.setObjectName("hSportLayout")
      self.vDepBox.addWidget(self.hSportLayoutWidget)

      self.lblSport = QLabel(self.hSportLayoutWidget)
      self.lblSport.setPixmap(QPixmap(BALL))
      self.lblSport.setAlignment(Qt.AlignCenter)
      self.hSportLayout.addWidget(self.lblSport)

      self.btnSport = QPushButton("Sport", self.hSportLayoutWidget)
      self.btnSport.setFont(QFont('AnyStyle', 15))
      self.btnSport.clicked.connect(self.SportClick)
      #self.btnSport.setStyleSheet("color : rgb(" + str(YELLOW.red()) + "," + str(YELLOW.green()) + "," + str(YELLOW.blue()) + ");")
      self.hSportLayout.addWidget(self.btnSport)

      self.hSportLayout.addWidget(QLabel(self))                       #Space

      #Books
      self.hBookLayoutWidget = QWidget(self)
      self.hBookLayoutWidget.setObjectName("hBookLayoutWidget")
      self.hBookLayoutWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.hBookLayout = QHBoxLayout(self.hBookLayoutWidget)
      self.hBookLayout.setObjectName("hBookLayout")
      self.vDepBox.addWidget(self.hBookLayoutWidget)

      self.lblBook = QLabel(self.hBookLayoutWidget)
      self.lblBook.setPixmap(QPixmap(BOOK))
      self.lblBook.setAlignment(Qt.AlignCenter)
      self.hBookLayout.addWidget(self.lblBook)

      self.btnBook= QPushButton("Books", self.hBookLayoutWidget)
      self.btnBook.setFont(QFont('AnyStyle', 15))
      self.btnBook.clicked.connect(self.BookClick)
      #self.btnBook.setStyleSheet("color : rgb(" + str(YELLOW.red()) + "," + str(YELLOW.green()) + "," + str(YELLOW.blue()) + ");")
      self.hBookLayout.addWidget(self.btnBook)

      self.hBookLayout.addWidget(QLabel(self))                       #Space

      #Clothing
      self.hClothingLayoutWidget = QWidget(self)
      self.hClothingLayoutWidget.setObjectName("hClothingLayoutWidget")
      self.hClothingLayoutWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.hClothingLayout = QHBoxLayout(self.hClothingLayoutWidget)
      self.hClothingLayout.setObjectName("hClothingLayout")
      self.vDepBox.addWidget(self.hClothingLayoutWidget)

      self.lblClothing = QLabel(self.hClothingLayoutWidget)
      self.lblClothing.setPixmap(QPixmap(SHIRT))
      self.lblClothing.setAlignment(Qt.AlignCenter)
      self.hClothingLayout.addWidget(self.lblClothing)

      self.btnClothing = QPushButton("Clothing", self.hClothingLayoutWidget)
      self.btnClothing.setFont(QFont('AnyStyle', 15))
      self.btnClothing.clicked.connect(self.ClothingClick)
      #self.btnClothing.setStyleSheet("color : rgb(" + str(YELLOW.red()) + "," + str(YELLOW.green()) + "," + str(YELLOW.blue()) + ");")
      self.hClothingLayout.addWidget(self.btnClothing)

      self.hClothingLayout.addWidget(QLabel(self))                       #Space

      #Electronics
      self.hElecLayoutWidget = QWidget(self)
      self.hElecLayoutWidget.setObjectName("hElecLayoutWidget")
      self.hElecLayoutWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.hElecLayout = QHBoxLayout(self.hElecLayoutWidget)
      self.hElecLayout.setObjectName("hElecLayout")
      self.vDepBox.addWidget(self.hElecLayoutWidget)

      self.lblElec = QLabel(self.hElecLayoutWidget)
      self.lblElec.setPixmap(QPixmap(MOUSE))
      self.lblElec.setAlignment(Qt.AlignCenter)
      self.hElecLayout.addWidget(self.lblElec)

      self.btnElec = QPushButton("Electronics", self.hElecLayoutWidget)
      self.btnElec.setFont(QFont('AnyStyle', 15))
      self.btnElec.clicked.connect(self.ElecClick)
      #self.btnElec.setStyleSheet("color : rgb(" + str(YELLOW.red()) + "," + str(YELLOW.green()) + "," + str(YELLOW.blue()) + ");")
      self.hElecLayout.addWidget(self.btnElec)

      self.hElecLayout.addWidget(QLabel(self))                       #Space


   def SportClick(self):
      self.lblIphone.setPixmap(QPixmap(BLANK))
      self.lblIT.setPixmap(QPixmap(BLANK))

   def BookClick(self):
      self.lblBag.setPixmap(self.imageIT)

      self.lblIphone.setPixmap(QPixmap(BLANK))
      self.lblCycle.setPixmap(QPixmap(BLANK))
      self.lblFootball.setPixmap(QPixmap(BLANK))
      self.lblGlasses.setPixmap(QPixmap(BLANK))
      self.lblIT.setPixmap(QPixmap(BLANK))

   def ClothingClick(self):
      self.lblBag.setPixmap(self.imageGlasses)

      self.lblIphone.setPixmap(QPixmap(BLANK))
      self.lblCycle.setPixmap(QPixmap(BLANK))
      self.lblFootball.setPixmap(QPixmap(BLANK))
      self.lblGlasses.setPixmap(QPixmap(BLANK))
      self.lblIT.setPixmap(QPixmap(BLANK))

   def ElecClick(self):
      self.lblBag.setPixmap(self.imageIphone)

      self.lblIphone.setPixmap(QPixmap(BLANK))
      self.lblCycle.setPixmap(QPixmap(BLANK))
      self.lblFootball.setPixmap(QPixmap(BLANK))
      self.lblGlasses.setPixmap(QPixmap(BLANK))
      self.lblIT.setPixmap(QPixmap(BLANK))

   def addItemGrid(self):
      self.itemGrid = itemGrid(self)
      
   def addMenu(self):
      self.menuAccount = self.menubar.addMenu('Account') #account menu tab
      self.menuAccount.setObjectName("menuAccount")
      if(not self.logged): #if they are logged in show all menu buttons
         #Account sub tabs
         self.actionAccountDetails = QAction('Details', self.menubar) #account details
         self.actionAccountDetails.setObjectName("actionAccountDetails")
         self.actionAccountDetails.triggered.connect(self.btnTemp)
         self.menuAccount.addAction(self.actionAccountDetails)

         self.actionTrack_Order = QAction('Track Order', self.menubar) #track order
         self.actionTrack_Order.setObjectName("actionTrack_Order")
         self.actionTrack_Order.triggered.connect(self.btnTemp)
         self.menuAccount.addAction(self.actionTrack_Order)

         self.actionLogout = QAction('Logout', self.menubar) #logout
         self.actionLogout.setObjectName("actionLogout")
         self.actionLogout.triggered.connect(self.Logout)
         self.menuAccount.addAction(self.actionLogout)
      
         #Wish List sub tabs
         self.menuWish_List = QAction('Wishlist', self.menubar)
         self.menuWish_List.setObjectName("menuWish_List")
         self.menuWish_List.triggered.connect(self.btnTemp)
         self.menubar.addAction(self.menuWish_List)

         #Cart sub tabs
         self.menuCart = QAction('Cart', self.menubar)
         self.menuCart.setObjectName("menuCart")
         self.menuCart.triggered.connect(self.btnCart_click)
         self.menubar.addAction(self.menuCart)

         #Sell sub tabs
         self.menuSell = QAction('Sell', self.menubar)
         self.menuSell.setObjectName("menuSell")
         self.menuSell.triggered.connect(self.btnTemp)
         self.menubar.addAction(self.menuSell)

      else:  #if they are not logged in show account and help
         self.actionLogin = QAction('Login', self.menubar) #Login sub button
         self.actionLogin.setObjectName("actionLogin")
         self.actionLogin.triggered.connect(self.btnLogin_clicked)
         self.menuAccount.addAction(self.actionLogin)

         self.actionRegister = QAction('Register', self.menubar) #Register sub button
         self.actionRegister.setObjectName("actionRegister")
         self.actionRegister.triggered.connect(self.btnRegister_clicked)
         self.menuAccount.addAction(self.actionRegister)

      self.menuHelp = QAction('Help', self.menubar) #Help main button
      self.menuHelp.setObjectName("menuHelp")
      self.menuHelp.triggered.connect(self.btnHelp_click)
      self.menubar.addAction(self.menuHelp)
   
   def addHeader(self):
      #Header text
      self.Header = QLabel("KIRBY'S MARKETPLACE", self)
      self.Header.setObjectName("Header")
      self.Header.setAlignment(Qt.AlignCenter)
      self.Header.setGeometry(QRect(LEFT_HEADER, TOP_HEADER, WIDTH_HEADER, HEIGHT_HEADER))

      self.pixmapHeader = QPixmap(HEADER_TITLE)
      self.Header.setPixmap(self.pixmapHeader) 

   def addSearch(self):
      self.hboxSearchWidget = QWidget(self)                    #Search
      self.hboxSearchWidget.setObjectName("hboxSearchWidget")
      self.hboxSearchWidget.setGeometry(QRect(LEFT_SEARCH, TOP_SEARCH, WIDTH_SEARCH, HEIGHT_SEARCH))
      self.hboxSearch = QHBoxLayout(self.hboxSearchWidget)
      self.hboxSearch.setObjectName("hboxSearch")
      self.hboxSearchWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.roundCorners(10.0, self.hboxSearchWidget)
      #self.hboxSearchWidget.move(QCursor.pos())                                    #Set object position to mouse position

      self.ledtSearch = QLineEdit(self.hboxSearchWidget)
      self.ledtSearch.setPlaceholderText("Search for products")
      self.ledtSearch.setMaximumHeight(HEIGHT_SEARCH)
      self.ledtSearch.setMinimumWidth(WIDTH_SEARCH - 65)
      self.ledtSearch.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + ");")
      self.roundCorners(6.0, self.ledtSearch)
      self.hboxSearch.addWidget(self.ledtSearch)

      self.btnSearch = QPushButton(self.hboxSearchWidget)
      self.btnSearch.setObjectName("btnSearch")
      self.btnSearch.setMinimumWidth(40)
      self.btnSearch.setMaximumHeight(HEIGHT_SEARCH)
      self.btnSearch.clicked.connect(self.btnTemp)
      self.btnSearch.setStyleSheet("background-image : url(" + SEARCH + ");")
      self.hboxSearch.addWidget(self.btnSearch)

   def addNewMenu(self):
      self.menubar.clear()
      self.logged = 0
      self.addMenu()

   def Logout(self):
      self.menubar.clear()
      self.logged = 1
      self.addMenu()
      print("Logout Successful")

   def btnLogin_clicked(self): #Open new Window when login button pressed
      self.mydialog = LoginWindow()
      self.mydialog.show()

   def btnRegister_clicked(self): #Open new Window when register button pressed
      self.mydialog = RegisterWindow()
      self.mydialog.show()

   #TODO: make functions for post login buttons
   def btnTemp(self): #Placeholder on click function for post login menu buttons
      print("Clicked")
   
   def btnCart_click(self): #Open cart window
      self.mydialog = CartWindow()
      self.mydialog.show()

   def btnWishlist_click(self): #Placeholder on click function for post login menu buttons
      self.mydialog = WishlistWindow()
      self.mydialog.show()
   
   def btnHelp_click(self): #Help button clicked
      #TODO: add help
      print("We are experiencing a high number of tickets, it will take longer than usual to get back to you")

#----------------------------------------------------------------------------------------------Subclass LoginWindow
class LoginWindow(Window): 
   def __init__(self):
      super().__init__()

      self.title = "Login"

      self.InitUI()
      self.addLoginWidgets()
   
   def addLoginWidgets(self):
      self.lblLoginHeader = QLabel(self)             #Login label
      self.pixmapHeader = QPixmap(LOGIN_TITLE)
      self.lblLoginHeader.setPixmap(self.pixmapHeader)
      self.vbox.addWidget(self.lblLoginHeader)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.vboxEmailWidget = QWidget(self)                    #Email
      self.vboxEmailWidget.setObjectName("vboxEmailWidget")
      self.vboxEmail = QVBoxLayout(self.vboxEmailWidget)
      self.vboxEmail.setObjectName("vboxEmail")
      self.vboxEmailWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxEmailWidget.setMinimumWidth(WIDTH_SUB_VBOX)
      self.vboxEmailWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxEmailWidget)
      self.vbox.addWidget(self.vboxEmailWidget)

      self.lblEmail= QLabel('Email', self.vboxEmailWidget)
      self.lblEmail.setFont(QFont('AnyStyle', 15))
      self.vboxEmail.addWidget(self.lblEmail)

      self.ledtEmail = QLineEdit(self.vboxEmailWidget)
      self.ledtEmail.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtEmail.setMinimumWidth(WIDTH_SUB_VBOX-20)
      self.ledtEmail.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtEmail)
      self.vboxEmail.addWidget(self.ledtEmail)

      self.vboxPassWidget = QWidget(self)                    #Password
      self.vboxPassWidget.setObjectName("vboxPassWidget")
      self.vboxPass = QVBoxLayout(self.vboxPassWidget)
      self.vboxPass.setObjectName("vboxPass")
      self.vbox.addWidget(self.vboxPassWidget)
      self.vboxPassWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxPassWidget.setMinimumWidth(WIDTH_SUB_VBOX)
      self.vboxPassWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxPassWidget)

      self.lblPass= QLabel('Password', self.vboxPassWidget)
      self.lblPass.setFont(QFont('AnyStyle', 15))
      self.vboxPass.addWidget(self.lblPass)

      self.ledtPass = QLineEdit(self.vboxPassWidget)
      self.ledtPass.setEchoMode(QLineEdit.Password)
      self.ledtPass.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtPass.setMinimumWidth(WIDTH_SUB_VBOX-20)
      self.ledtPass.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtPass)
      self.vboxPass.addWidget(self.ledtPass)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.hboxWidget = QWidget(self)                         #Login  
      self.hboxWidget.setObjectName("hboxWidget")
      self.hbox = QVBoxLayout(self.hboxWidget)
      self.hbox.setContentsMargins(MARGIN_BUTTON, 0, MARGIN_BUTTON, 0)
      self.hbox.setObjectName("hbox")
      self.vbox.addWidget(self.hboxWidget)

      self.btnLogin = QPushButton(self.hboxWidget)            #Login Button
      self.btnLogin.setObjectName("btnLogin")
      self.btnLogin.setText("Login")
      self.btnLogin.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.btnLogin.setMinimumWidth(2*MARGIN_BUTTON)
      self.btnLogin.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(6.0, self.btnLogin)
      self.btnLogin.clicked.connect(self.btnLogin_clicked)
      self.hbox.addWidget(self.btnLogin)

   def btnLogin_clicked(self): #check login details
      email = self.ledtEmail.text()
      password = self.ledtPass.text()
      logged = login(email, password)
      
      if(not logged):
         user = currUser(email=email)
         print("Login successful")
         ex.addNewMenu()
         self.close()
      elif(logged==1):
         print("Incorrect details")
      elif(logged==-1):
         print("There was an external error")
      
#----------------------------------------------------------------------------------------------Subclass RegisterWindow
class RegisterWindow(Window): 

   def __init__(self):
      super().__init__()

      self.title = "Register"

      self.InitUI()
      self.addRegisterWidgets()
   
   def addRegisterWidgets(self):
      self.lblRegisterHeader = QLabel(self)             #Register label
      self.pixmapHeader = QPixmap(REGISTER_TITLE)
      self.lblRegisterHeader.setPixmap(self.pixmapHeader)
      self.vbox.addWidget(self.lblRegisterHeader)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.vboxFNameWidget = QWidget(self)                    #First Name
      self.vboxFNameWidget.setObjectName("vboxFNameWidget")
      self.vboxFName = QVBoxLayout(self.vboxFNameWidget)
      self.vboxFName.setObjectName("vboxFName")
      self.vboxFNameWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxFNameWidget.setMinimumWidth(self.pixmapHeader.width())
      self.vboxFNameWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxFNameWidget)
      self.vbox.addWidget(self.vboxFNameWidget)

      self.lblFName= QLabel('First Name', self.vboxFNameWidget)
      self.lblFName.setFont(QFont('AnyStyle', 15))
      self.vboxFName.addWidget(self.lblFName)

      self.ledtFName = QLineEdit(self.vboxFNameWidget)
      self.ledtFName.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtFName.setMinimumWidth(int(19*self.pixmapHeader.width()/20))
      self.ledtFName.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtFName)
      self.vboxFName.addWidget(self.ledtFName)

      self.vboxSurnameWidget = QWidget(self)                    #Surname
      self.vboxSurnameWidget.setObjectName("vboxSurnameWidget")
      self.vboxSurname = QVBoxLayout(self.vboxSurnameWidget)
      self.vboxSurname.setObjectName("vboxSurname")
      self.vboxSurnameWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxSurnameWidget.setMinimumWidth(self.pixmapHeader.width())
      self.vboxSurnameWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxSurnameWidget)
      self.vbox.addWidget(self.vboxSurnameWidget)

      self.lblSurname= QLabel('Surname', self.vboxSurnameWidget)
      self.lblSurname.setFont(QFont('AnyStyle', 15))
      self.vboxSurname.addWidget(self.lblSurname)

      self.ledtSurname = QLineEdit(self.vboxSurnameWidget)
      self.ledtSurname.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtSurname.setMinimumWidth(int(19*self.pixmapHeader.width()/20))
      self.ledtSurname.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtSurname)
      self.vboxSurname.addWidget(self.ledtSurname)

      self.vboxEmailWidget = QWidget(self)                    #Email
      self.vboxEmailWidget.setObjectName("vboxEmailWidget")
      self.vboxEmail = QVBoxLayout(self.vboxEmailWidget)
      self.vboxEmail.setObjectName("vboxEmail")
      self.vboxEmailWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxEmailWidget.setMinimumWidth(self.pixmapHeader.width())
      self.vboxEmailWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxEmailWidget)
      self.vbox.addWidget(self.vboxEmailWidget)

      self.lblEmail= QLabel('Email', self.vboxEmailWidget)
      self.lblEmail.setFont(QFont('AnyStyle', 15))
      self.vboxEmail.addWidget(self.lblEmail)

      self.ledtEmail = QLineEdit(self.vboxEmailWidget)
      self.ledtEmail.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtEmail.setMinimumWidth(int(19*self.pixmapHeader.width()/20))
      self.ledtEmail.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtEmail)
      self.vboxEmail.addWidget(self.ledtEmail)

      self.vboxPassWidget = QWidget(self)                    #Password
      self.vboxPassWidget.setObjectName("vboxPassWidget")
      self.vboxPass = QVBoxLayout(self.vboxPassWidget)
      self.vboxPass.setObjectName("vboxPass")
      self.vboxPassWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxPassWidget.setMinimumWidth(self.pixmapHeader.width())
      self.vboxPassWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxPassWidget)
      self.vbox.addWidget(self.vboxPassWidget)

      self.lblPass= QLabel('Password', self.vboxPassWidget)
      self.lblPass.setFont(QFont('AnyStyle', 15))
      self.vboxPass.addWidget(self.lblPass)

      self.ledtPass = QLineEdit(self.vboxPassWidget)
      self.ledtPass.setEchoMode(QLineEdit.Password)
      self.ledtPass.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtPass.setMinimumWidth(int(19*self.pixmapHeader.width()/20))
      self.ledtPass.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtPass)
      self.vboxPass.addWidget(self.ledtPass)

      self.vboxPass2Widget = QWidget(self)                    #Password Retype
      self.vboxPass2Widget.setObjectName("vboxPass2Widget")
      self.vboxPass2 = QVBoxLayout(self.vboxPass2Widget)
      self.vboxPass2.setObjectName("vboxPass2")
      self.vboxPass2Widget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      self.vboxPass2Widget.setMinimumWidth(self.pixmapHeader.width())
      self.vboxPass2Widget.setMinimumHeight(HEIGHT_SUB_VBOX)
      self.roundCorners(15.0, self.vboxPass2Widget)
      self.vbox.addWidget(self.vboxPass2Widget)

      self.lblPass2= QLabel('Retype Password', self.vboxPass2Widget)
      self.lblPass2.setFont(QFont('AnyStyle', 15))
      self.vboxPass2.addWidget(self.lblPass2)

      self.ledtPass2 = QLineEdit(self.vboxPass2Widget)
      self.ledtPass2.setEchoMode(QLineEdit.Password)
      self.ledtPass2.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      self.ledtPass2.setMinimumWidth(int(19*self.pixmapHeader.width()/20))
      self.ledtPass2.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, self.ledtPass2)
      self.vboxPass2.addWidget(self.ledtPass2)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.hboxWidget = QWidget(self)                         #Register 
      self.hboxWidget.setObjectName("hboxWidget")
      self.hbox = QVBoxLayout(self.hboxWidget)
      self.hbox.setContentsMargins(MARGIN_BUTTON, 0, MARGIN_BUTTON, 0)
      self.hbox.setObjectName("hbox")
      self.vbox.addWidget(self.hboxWidget)

      self.btnRegister = QPushButton(self.hboxWidget)            #Register Button
      self.btnRegister.setObjectName("btnRegister")
      self.btnRegister.setText("Register")
      self.btnRegister.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.btnRegister.setMinimumWidth(4*MARGIN_BUTTON)
      self.btnRegister.setMaximumHeight(int(HEIGHT_SUB_VBOX/4))
      self.roundCorners(6.0, self.btnRegister)
      self.btnRegister.clicked.connect(self.btnRegister_clicked)
      self.hbox.addWidget(self.btnRegister)

   def btnRegister_clicked(self): #check login details
      fname = self.ledtFName.text()
      fNameCheck = checkFName(fname)
      if(fNameCheck==1):
         print("First name too long")
         return 1
      elif(fNameCheck==2):
         print("First name too short")
         return 2
      elif(fNameCheck==3):
         print("First name cannot contain special characters")
         return 3

      surname = self.ledtSurname.text()
      surnameCheck = checkSurname(surname)
      if(surnameCheck==1):
         print("Surname too long")
         return 1
      elif(surnameCheck==2):
         print("Surname too short")
         return 2
      elif(surnameCheck==3):
         print("Surname cannot contain special characters")
         return 3

      email = self.ledtEmail.text()
      emailCheck = checkEmail(email)
      if(emailCheck==1):
         print("Email too long")
         return 1
      elif(emailCheck==2):
         print("Email too short")
         return 2
      elif(emailCheck==3):
         print("Email cannot contain special characters")
         return 3
      elif(emailCheck==4):
         print("Email does not contain @")
         return 4

      password = self.ledtPass.text()
      password2 = self.ledtPass2.text()
      
      if(password!=password2):
         print("Passwords do not match")
      else:
         snhpassword, salt = encrypt(password)
         reg = register(fname,surname,email,snhpassword, salt)
         if(not reg):
            user = currUser(email=email)
            print("Successfully Registered")
            ex.addNewMenu()
            self.close()
         else:
            print("There was an error registering")
      
      logged = login(email, password)


ex = MainWindow() #create MainWindow object

#-------------------------------------------------------------------------------------Cart window
class CartWindow(Window):
   def __init__(self):
      super().__init__()
      self.title = "Cart"
      self.InitUI()
      self.setGeometry(QRect(LEFT_CART_WINDOW,TOP_CART_WINDOW,WIDTH_CART_WINDOW,HEIGHT_CART_WINDOW))
      self.vbox.setContentsMargins(MARGIN_CART_WINDOW_SIDES,MARGIN_CART_WINDOW_BOTTOM,MARGIN_CART_WINDOW_SIDES,MARGIN_CART_WINDOW_BOTTOM)
      self.vbox.setGeometry(QRect(LEFT_CART_WINDOW,TOP_CART_WINDOW,WIDTH_CART_WINDOW,HEIGHT_CART_WINDOW))
      self.addCartWidgets()

   def addCartWidgets(self):
      self.hHeaderWidget = QWidget(self)                    #Header HBox widget
      self.hHeaderWidget.setObjectName("hHeaderWidget")
      self.hHeaderWidget.setMinimumWidth(WIDTH_CART_BOX)
      self.hHeader = QHBoxLayout(self.hHeaderWidget)
      self.hHeader.setObjectName("hHeader")
      self.vbox.addWidget(self.hHeaderWidget)

      self.lblCartHeader = QLabel(self)             #Register label
      self.pixmapHeader = QPixmap(CART_TITLE)
      self.lblCartHeader.setPixmap(self.pixmapHeader)
      self.lblCartHeader.setAlignment(Qt.AlignLeft)
      self.hHeader.addWidget(self.lblCartHeader)

      self.hHeader.addWidget(QLabel(self)) #spaces
      self.hHeader.addWidget(QLabel(self))

      self.vCheckoutWidget = QWidget(self)                    #Total & Checkout Box
      self.vCheckoutWidget.setObjectName("vCheckoutWidget")
      self.vCheckoutWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vCheckoutWidget.setMinimumWidth(WIDTH_CHECKOUT_BOX)
      self.vCheckoutWidget.setMinimumHeight(HEIGHT_CHECKOUT_BOX)
      self.roundCorners(10.0, self.vCheckoutWidget)
      self.vCheckout = QVBoxLayout(self.vCheckoutWidget)
      self.vCheckout.setObjectName("vCheckout")
      self.vCheckout.setAlignment(Qt.AlignRight)
      self.hHeader.addWidget(self.vCheckoutWidget)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.vCartWidget = QWidget(self)                    #Cart items
      self.vCartWidget.setObjectName("vCartWidget")
      self.vCartWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vCartWidget.setMinimumHeight(HEIGHT_CART_BOX)
      self.vCartWidget.setMinimumWidth(WIDTH_CART_BOX)
      self.roundCorners(10.0, self.vCartWidget)
      self.vCart = QVBoxLayout(self.vCartWidget)
      self.vCart.setObjectName("vCart")
      self.vbox.addWidget(self.vCartWidget)
      






#-------------------------------------------------------------------------------------Start Program
def createMain():
   app = QApplication(sys.argv)          
   ex.showMaximized()
   sys.exit(app.exec_())
