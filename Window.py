import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *
from database import register, login
from user import *
from login.encrypter import encrypt
from login.verification import *
from ItemGrid import *
from cart import *

#-------------------------------------------------------------------------------------Base Class Window
class Window(QWidget):  
   def __init__(self):
      super ().__init__()

      self.title = "Kirby's Marketplace" #define window attributes
      self.left = LEFT_SUB
      self.top = TOP_SUB
      self.widgetWidth1 = WIDTH_SUB_VBOX
      self.widgetWidth2 = int(4*WIDTH_SUB_VBOX/5)
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

   def addInputWidget(self, text, **kwargs):
      password = kwargs.get('isPass', False)

      vboxWidget = QWidget(self)                    #Vbox 
      vboxWidget.setObjectName("vboxWidget")
      vboxWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); border-style: outset;")
      vboxWidget.setMinimumWidth(self.widgetWidth1)
      vboxWidget.setMinimumHeight(HEIGHT_SUB_VBOX)
      vboxInput = QVBoxLayout(vboxWidget)
      vboxInput.setObjectName("vboxInput")
      self.roundCorners(15.0, vboxWidget)
      self.vbox.addWidget(vboxWidget)

      lblTitle= QLabel(text, vboxWidget)     #Title
      lblTitle.setFont(QFont('AnyStyle', 15))
      vboxInput.addWidget(lblTitle)

      ledtInput = QLineEdit(vboxWidget)    #Input box
      ledtInput.setStyleSheet("background-color: rgb(" + str(WHITE.red()) + "," + str(WHITE.green()) + "," + str(WHITE.blue()) + "); padding: 4px;")
      if password: ledtInput.setEchoMode(QLineEdit.Password)
      ledtInput.setMinimumWidth(self.widgetWidth2)
      ledtInput.setMaximumHeight(int(HEIGHT_SUB_VBOX/3))
      self.roundCorners(8.0, ledtInput)
      vboxInput.addWidget(ledtInput)
      return ledtInput

#-----------------------------------------------------------------------------------------Subclass MainWindow
class MainWindow(Window): 
   def __init__(self):
      super().__init__()

      self.width = WIDTH_MAIN
      self.height = HEIGHT_MAIN
      
      self.logged = 1 #0=logged in, 1=not logged in
      self.menubar = QMenuBar(self)
      self.menubar.setGeometry(QRect(0, 0, 1115, 20))
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
      self.lblSport.setCursor(Qt.PointingHandCursor)
      self.hSportLayout.addWidget(self.lblSport)

      self.btnSport = QPushButton("Sport", self.hSportLayoutWidget)
      self.btnSport.setFont(QFont('AnyStyle', 15))
      self.btnSport.clicked.connect(self.SportClick)
      self.btnSport.setCursor(Qt.PointingHandCursor)
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
      self.lblBook.setCursor(Qt.PointingHandCursor)
      self.hBookLayout.addWidget(self.lblBook)

      self.btnBook= QPushButton("Books", self.hBookLayoutWidget)
      self.btnBook.setFont(QFont('AnyStyle', 15))
      self.btnBook.clicked.connect(self.BookClick)
      self.btnBook.setCursor(Qt.PointingHandCursor)
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
      self.lblClothing.setCursor(Qt.PointingHandCursor)
      self.hClothingLayout.addWidget(self.lblClothing)

      self.btnClothing = QPushButton("Clothing", self.hClothingLayoutWidget)
      self.btnClothing.setFont(QFont('AnyStyle', 15))
      self.btnClothing.clicked.connect(self.ClothingClick)
      self.btnClothing.setCursor(Qt.PointingHandCursor)
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
      self.lblElec.setCursor(Qt.PointingHandCursor)
      self.hElecLayout.addWidget(self.lblElec)

      self.btnElec = QPushButton("Electronics", self.hElecLayoutWidget)
      self.btnElec.setFont(QFont('AnyStyle', 15))
      self.btnElec.clicked.connect(self.ElecClick)
      self.btnElec.setCursor(Qt.PointingHandCursor)
      self.hElecLayout.addWidget(self.btnElec)

      self.hElecLayout.addWidget(QLabel(self))                       #Space


   def SportClick(self):
      self.itemGrid.sortBy("Sports")

   def BookClick(self):
      self.itemGrid.sortBy("Books")

   def ClothingClick(self):
      self.itemGrid.sortBy("Clothing")

   def ElecClick(self):
      self.itemGrid.sortBy("Electronics")

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
         self.menuWish_List.triggered.connect(self.btnWishlist_click)
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
      self.btnSearch.setCursor(Qt.PointingHandCursor)
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
      try:
         self.mydialog.close()
         self.mydialog = CartWindow()
         self.mydialog.show()
      except:
         self.mydialog = CartWindow()
         self.mydialog.show()
      

   def btnWishlist_click(self): #Open wishlist window
      try:
         self.mydialog.close()
         self.mydialog = WishlistWindow()
         self.mydialog.show()
      except:
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
      self.widgetWidth1 = WIDTH_SUB_VBOX          #set widget width
      self.widgetWidth2 = WIDTH_SUB_VBOX-20

      self.InitUI()
      self.addLoginWidgets()
   
   def addLoginWidgets(self):
      self.lblLoginHeader = QLabel(self)             #Login label
      self.pixmapHeader = QPixmap(LOGIN_TITLE)
      self.lblLoginHeader.setPixmap(self.pixmapHeader)
      self.lblLoginHeader.setAlignment(Qt.AlignHCenter)
      self.vbox.addWidget(self.lblLoginHeader)
      
      self.vbox.addWidget(QLabel(self))                       #Space

      self.ledtEmail = self.addInputWidget("Email")           #Email

      self.ledtPass = self.addInputWidget("Password", isPass=True)   #Password

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
      self.btnLogin.setFont(QFont('AnyStyle', 14))
      self.btnLogin.setMinimumWidth(2*MARGIN_BUTTON)
      self.roundCorners(6.0, self.btnLogin)
      self.btnLogin.clicked.connect(self.btnLogin_clicked)
      self.btnLogin.setCursor(Qt.PointingHandCursor)
      self.hbox.addWidget(self.btnLogin)

   def btnLogin_clicked(self): #check login details
      email = self.ledtEmail.text()
      password = self.ledtPass.text()
      logged = login(email, password)
      
      if(not logged):
         myUser.Login(email)
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

      self.widgetWidth1 = self.pixmapHeader.width()          #set widget width
      self.widgetWidth2 = int(19*self.widgetWidth1/20)
      self.vbox.addWidget(QLabel(self))                      #Space
             
      self.ledtFName = self.addInputWidget("First Name")     #First Name
      
      self.ledtSurname = self.addInputWidget("Surname")      #Surname

      self.ledtEmail = self.addInputWidget("Email")          #Email

      self.ledtPassword1 = self.addInputWidget("Password", isPass=True)          #Password

      self.ledtPassword2 = self.addInputWidget("Confirm Password", isPass=True)  #Confirm Password
      
      self.vbox.addWidget(QLabel(self))                       #Space

      self.hboxWidget = QWidget(self)                         #Register 
      self.hboxWidget.setObjectName("hboxWidget")
      self.hbox = QVBoxLayout(self.hboxWidget)
      self.hbox.setContentsMargins(MARGIN_BUTTON, 0, MARGIN_BUTTON, 0)
      self.hbox.setObjectName("hbox")
      self.vbox.addWidget(self.hboxWidget)

      self.btnRegister = QPushButton("Register", self.hboxWidget)            #Register Button
      self.btnRegister.setObjectName("btnRegister")
      self.btnRegister.setFont(QFont('AnyStyle', 14))
      self.btnRegister.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.btnRegister.setMinimumWidth(4*MARGIN_BUTTON)
      self.roundCorners(6.0, self.btnRegister)
      self.btnRegister.clicked.connect(self.btnRegister_clicked)
      self.btnRegister.setCursor(Qt.PointingHandCursor)
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

      password = self.ledtPassword1.text()
      password2 = self.ledtPassword2.text()
      
      if(password!=password2):
         print("Passwords do not match")
      else:
         snhpassword, salt = encrypt(password)
         reg = register(fname,surname,email,snhpassword, salt)
         if(not reg):
            myUser.Login(email)
            print("Successfully Registered")
            ex.addNewMenu()
            self.close()
         else:
            print("There was an error registering")
      
      self.logged = login(email, password)

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
      self.roundCorners(9.0, self.vCheckoutWidget)
      self.vCheckout = QVBoxLayout(self.vCheckoutWidget)
      self.vCheckout.setObjectName("vCheckout")
      self.vCheckout.setAlignment(Qt.AlignTop)
      self.hHeader.addWidget(self.vCheckoutWidget)

      #total cost label
      self.lblTotal = QLabel("Total:  (" + str(len(myCart.cartList)) + " items)  R" + str(myCart.totalCost), self)
      self.lblTotal.setFont(QFont('AnyStyle', 14))
      self.vCheckout.addWidget(self.lblTotal)

      self.btncheckout = QPushButton("Checkout", self) #checkout button
      self.btncheckout.setObjectName("btnCheckout")
      self.btncheckout.setFont(QFont('AnyStyle', 12))
      self.btncheckout.setMinimumWidth(WIDTH_CHECKOUT_BUTTON)
      self.btncheckout.setMaximumHeight(HEIGHT_CHECKOUT_BUTTON-10)
      self.btncheckout.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.roundCorners(6.0, self.btncheckout)
      self.btncheckout.clicked.connect(self.btnCheckoutClick)
      self.btncheckout.setCursor(Qt.PointingHandCursor)
      self.vCheckout.addWidget(self.btncheckout)

      self.vbox.addWidget(QLabel(self))                       #Space

      height_grid_scroll = len(myCart.cartList) * MAX_HEIGHT_ITEM_CART +20

      self.vCartWidget = QWidget(self)                    #Cart items
      self.vCartWidget.setObjectName("vCartWidget")
      self.vCartWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))
      self.roundCorners(10.0, self.vCartWidget)
      self.vCart = QVBoxLayout(self.vCartWidget)
      self.vCart.setObjectName("vCart")

      self.scrollArea = QScrollArea(self) #scrollable grid
      self.scrollArea.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 8px; border-style: outset;")
      self.scrollArea.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX, HEIGHT_CART_BOX))
      self.scrollArea.setWidget(self.vCartWidget)
      self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
      self.roundCorners(10.0, self.scrollArea)
      
      for myProduct in myCart.cartList:
         self.addNewItem(myCart.get_item(myProduct))

   def addNewItem(self, item):
      def removeItem(event):
         myCart.remove_item(item[0])
         self.updateCost()

         for i in reversed(range(self.vCart.count())): 
            self.vCart.itemAt(i).widget().setParent(None)

         height_grid_scroll = len(myCart.cartList) * MAX_HEIGHT_ITEM_CART +20
         self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))
            
         for myProduct in myCart.cartList:
            self.addNewItem(myCart.get_item(myProduct))

      def moveToWishlist(event):
         myWishlist.add_item(myCart.get_item(item[0]))
         myCart.remove_item(item[0])
         self.updateCost()

         for i in reversed(range(self.vCart.count())): 
            self.vCart.itemAt(i).widget().setParent(None)

         height_grid_scroll = len(myCart.cartList) * MAX_HEIGHT_ITEM_CART +20
         self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))

         for myProduct in myCart.cartList:
            self.addNewItem(myCart.get_item(myProduct))

      hItemBoxWidget = QWidget(self) #horizontal layout to store item info
      hItemBoxWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      hItemBoxWidget.setMaximumHeight(MAX_HEIGHT_ITEM_CART)
      hItemBox = QHBoxLayout(hItemBoxWidget)  
      self.vCart.addWidget(hItemBoxWidget)

      #image
      mainImage = QPixmap(item[5])
      lblProduct = QLabel(self)
      lblProduct.setMaximumSize(MAX_HEIGHT_ITEM_CART,MAX_HEIGHT_ITEM_CART)
      lblProduct.setPixmap(mainImage)
      lblProduct.setScaledContents(True)
      hItemBox.addWidget(lblProduct)

      #name and price 
      vNameWidget = QWidget(self) #vertical layout to store item info
      vNameWidget.setObjectName("vNameWidget")
      vName = QVBoxLayout(vNameWidget)
      vName.setObjectName("vName")
      hItemBox.addWidget(vNameWidget)

      lblName = QLabel(item[1], vNameWidget)
      lblName.setFont(QFont('AnyStyle', 14))
      vName.addWidget(lblName)

      lblPrice = QLabel("R" + str(item[2]), vNameWidget)
      lblPrice.setFont(QFont('AnyStyle', 14))
      vName.addWidget(lblPrice)

      #move to wishlist
      hRightButtonsWidget = QWidget(self) #horizontal layout to store far buttons
      hRightButtons = QHBoxLayout(hRightButtonsWidget)
      hRightButtons.setAlignment(Qt.AlignRight)
      hItemBox.addWidget(hRightButtonsWidget)

      vWishWidget = QWidget(self) #vertical layout to store item info
      vWish = QVBoxLayout(vWishWidget)
      vWish.setAlignment(Qt.AlignRight)
      hRightButtons.addWidget(vWishWidget)

      lblWish = QLabel(self)                     #Wish Icon
      lblWish.setPixmap(QPixmap(WISHLIST))
      lblWish.setAlignment(Qt.AlignHCenter)
      lblWish.setCursor(Qt.PointingHandCursor)
      lblWish.mousePressEvent = moveToWishlist
      vWish.addWidget(lblWish)

      lblWishText = QLabel("Wishlist instead", self)          #Wish text
      lblWishText.setFont(QFont('AnyStyle', 12))
      lblWishText.setAlignment(Qt.AlignHCenter)
      lblWishText.setCursor(Qt.PointingHandCursor)
      lblWishText.mousePressEvent = moveToWishlist
      vWish.addWidget(lblWishText)

      #remove
      vRemoveWidget = QWidget(self) #vertical layout to store item info
      vRemove = QVBoxLayout(vRemoveWidget)
      vRemove.setAlignment(Qt.AlignRight)
      hRightButtons.addWidget(vRemoveWidget)

      lblBin = QLabel(self)                           #Remove Icon
      lblBin.setPixmap(QPixmap(BIN))
      lblBin.mousePressEvent = removeItem
      lblBin.setAlignment(Qt.AlignHCenter)
      lblBin.setCursor(Qt.PointingHandCursor)
      vRemove.addWidget(lblBin)

      lblRemoveText = QLabel("Remove", self)       #Remove text
      lblRemoveText.setFont(QFont('AnyStyle', 12))
      lblRemoveText.setAlignment(Qt.AlignHCenter)
      lblRemoveText.mousePressEvent = removeItem
      lblRemoveText.setCursor(Qt.PointingHandCursor)
      vRemove.addWidget(lblRemoveText)

   def btnCheckoutClick(self):
      self.myDialog = CheckoutWindow()
      self.myDialog.show()
      self.close() #TODO: Should it close cart window or nah?

   def updateCost(self):
      self.lblTotal.setText("Total:  (" + str(len(myCart.cartList)) + " items)  R" + str(myCart.totalCost))

#-------------------------------------------------------------------------------------Checkout window
class CheckoutWindow(Window):
   def __init__(self):
      super ().__init__()
      self.title = "Checkout"
      self.addHeader()
      self.addWidgets()
      
   def addHeader(self):                                           #Details header label
      self.lblCheckoutHeader = QLabel(self)             
      self.pixmapHeader = QPixmap(CHECKOUT_TITLE)
      self.lblCheckoutHeader.setPixmap(self.pixmapHeader)
      self.lblCheckoutHeader.setAlignment(Qt.AlignHCenter)
      self.vbox.addWidget(self.lblCheckoutHeader)

      self.widgetWidth1 = self.pixmapHeader.width()               #set widget width
      self.widgetWidth2 = int(19*self.widgetWidth1/20)

   def addWidgets(self):
      self.vbox.setAlignment(Qt.AlignTop)
      self.vbox.addWidget(QLabel())                           #Space
      self.vbox.addWidget(QLabel())

      self.ledtName = self.addInputWidget("Name & Surname")       #Name & Surname
      self.ledtName.setText(myUser.get_Name() + " " + myUser.get_Surname())

      self.ledtEmail = self.addInputWidget("Email")               #Email
      self.ledtEmail.setText(myUser.get_Email())

      self.ledtCellNumber = self.addInputWidget("Cell Number")    #Cell Number

      self.ledtProvince = self.addInputWidget("Province")         #Province
      self.cbProvince = QComboBox(self.ledtProvince)
      self.cbProvince.addItems(PROVINCES)
      self.cbProvince.setMinimumWidth(self.widgetWidth2)
      self.roundCorners(8.0, self.cbProvince)
      self.ledtProvince.setCursor(Qt.PointingHandCursor)

      self.ledtAddress = self.addInputWidget("Address")           #Address

      self.ledtPostalCode = self.addInputWidget("Postal Code")    #Postal Code

      self.vbox.addWidget(QLabel())                           #Space

      self.vCheckoutWidget = QWidget(self)                    #Total & Checkout Box
      self.vCheckoutWidget.setObjectName("vCheckoutWidget")
      self.vCheckoutWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vCheckoutWidget.setMinimumWidth(self.widgetWidth1)
      self.vCheckoutWidget.setMinimumHeight(HEIGHT_CHECKOUT_BOX)
      self.roundCorners(9.0, self.vCheckoutWidget)
      self.vCheckout = QVBoxLayout(self.vCheckoutWidget)
      self.vCheckout.setObjectName("vCheckout")
      self.vCheckout.setAlignment(Qt.AlignHCenter)
      self.vbox.addWidget(self.vCheckoutWidget)

      #total cost label
      self.lblTotal = QLabel("Total:  (" + str(len(myCart.cartList)) + " items)  R" + str(myCart.totalCost), self)
      self.lblTotal.setFont(QFont('AnyStyle', 14))
      self.vCheckout.addWidget(self.lblTotal)

      self.btncheckout = QPushButton("Checkout", self) #checkout button
      self.btncheckout.setObjectName("btnCheckout")
      self.btncheckout.setFont(QFont('AnyStyle', 12))
      self.btncheckout.setMinimumWidth(WIDTH_CHECKOUT_BUTTON)
      self.btncheckout.setMaximumHeight(HEIGHT_CHECKOUT_BUTTON-10)
      self.btncheckout.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + ");")
      self.roundCorners(6.0, self.btncheckout)
      self.btncheckout.clicked.connect(self.btnCheckoutClick)
      self.btncheckout.setCursor(Qt.PointingHandCursor)
      self.vCheckout.addWidget(self.btncheckout)

   def btnCheckoutClick(self):
      print("Thank you for shopping!")

#-------------------------------------------------------------------------------------Wishlist window
class WishlistWindow(Window):
   def __init__(self):
      super().__init__()
      self.title = "Wishlist"

      self.InitUI()
      self.setGeometry(QRect(LEFT_CART_WINDOW,TOP_CART_WINDOW,WIDTH_CART_WINDOW,HEIGHT_CART_WINDOW))
      self.vbox.setContentsMargins(MARGIN_CART_WINDOW_SIDES,MARGIN_CART_WINDOW_BOTTOM,MARGIN_CART_WINDOW_SIDES,MARGIN_CART_WINDOW_BOTTOM)
      self.vbox.setGeometry(QRect(LEFT_CART_WINDOW,TOP_CART_WINDOW,WIDTH_CART_WINDOW,HEIGHT_CART_WINDOW))
      self.addWishlistWidgets()

   def addWishlistWidgets(self):
      self.lblCartHeader = QLabel(self)             #Register label
      self.pixmapHeader = QPixmap(WISHLIST_TITLE)
      self.lblCartHeader.setPixmap(self.pixmapHeader)
      self.lblCartHeader.setAlignment(Qt.AlignLeft)
      self.vbox.addWidget(self.lblCartHeader)

      self.vbox.addWidget(QLabel(self))                       #Space

      height_grid_scroll = len(myWishlist.wishlist) * MAX_HEIGHT_ITEM_CART +20

      self.vCartWidget = QWidget(self)                    #Cart items
      self.vCartWidget.setObjectName("vCartWidget")
      self.vCartWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))
      self.roundCorners(10.0, self.vCartWidget)
      self.vCart = QVBoxLayout(self.vCartWidget)
      self.vCart.setObjectName("vCart")

      self.scrollArea = QScrollArea(self) #scrollable grid
      self.scrollArea.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 8px; border-style: outset;")
      self.scrollArea.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX, HEIGHT_CART_BOX))
      self.scrollArea.setWidget(self.vCartWidget)
      self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
      self.roundCorners(10.0, self.scrollArea)
      
      for myProduct in myWishlist.wishlist:
         self.addNewItem(myWishlist.get_item(myProduct))

   def addNewItem(self, item):
      def removeItem(event):
         myWishlist.remove_item(item[0])

         for i in reversed(range(self.vCart.count())): 
            self.vCart.itemAt(i).widget().setParent(None)

         height_grid_scroll = len(myWishlist.wishlist) * MAX_HEIGHT_ITEM_CART +20
         self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))
            
         for myProduct in myWishlist.wishlist:
            self.addNewItem(myWishlist.get_item(myProduct))

      def addtoCart(event):
         myCart.add_item(myWishlist.get_item(item[0]))
         myWishlist.remove_item(item[0])

         for i in reversed(range(self.vCart.count())): 
            self.vCart.itemAt(i).widget().setParent(None)

         height_grid_scroll = len(myWishlist.wishlist) * MAX_HEIGHT_ITEM_CART +20
         self.vCartWidget.setGeometry(QRect(LEFT_CART_BOX, TOP_CART_BOX, WIDTH_CART_BOX-20, height_grid_scroll))

         for myProduct in myWishlist.wishlist:
            self.addNewItem(myWishlist.get_item(myProduct))

      hItemBoxWidget = QWidget(self) #horizontal layout to store item info
      hItemBoxWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      hItemBoxWidget.setMaximumHeight(MAX_HEIGHT_ITEM_CART)
      hItemBox = QHBoxLayout(hItemBoxWidget)  
      self.vCart.addWidget(hItemBoxWidget)

      #image
      mainImage = QPixmap(item[5])
      lblProduct = QLabel(self)
      lblProduct.setMaximumSize(MAX_HEIGHT_ITEM_CART,MAX_HEIGHT_ITEM_CART)
      lblProduct.setPixmap(mainImage)
      lblProduct.setScaledContents(True)
      hItemBox.addWidget(lblProduct)

      #name and price 
      vNameWidget = QWidget(self) #vertical layout to store item info
      vNameWidget.setObjectName("vNameWidget")
      vName = QVBoxLayout(vNameWidget)
      vName.setObjectName("vName")
      hItemBox.addWidget(vNameWidget)

      lblName = QLabel(item[1], vNameWidget)
      lblName.setFont(QFont('AnyStyle', 14))
      vName.addWidget(lblName)

      lblPrice = QLabel("R" + str(item[2]), vNameWidget)
      lblPrice.setFont(QFont('AnyStyle', 14))
      vName.addWidget(lblPrice)

      #add to cart
      hRightButtonsWidget = QWidget(self) #horizontal layout to store far buttons
      hRightButtons = QHBoxLayout(hRightButtonsWidget)
      hRightButtons.setAlignment(Qt.AlignRight)
      hItemBox.addWidget(hRightButtonsWidget)

      vWishWidget = QWidget(self) #vertical layout to store item info
      vWish = QVBoxLayout(vWishWidget)
      vWish.setAlignment(Qt.AlignCenter)
      hRightButtons.addWidget(vWishWidget)

      lblWish = QLabel(self)                     #Wish Icon
      lblWish.setPixmap(QPixmap(CART))
      lblWish.setAlignment(Qt.AlignHCenter)
      lblWish.mousePressEvent = addtoCart
      lblWish.setCursor(Qt.PointingHandCursor)
      vWish.addWidget(lblWish)

      lblWishText = QLabel("Add to Cart", self)          #Wish text
      lblWishText.setFont(QFont('AnyStyle', 12))
      lblWishText.setAlignment(Qt.AlignHCenter)
      lblWishText.mousePressEvent = addtoCart
      lblWishText.setCursor(Qt.PointingHandCursor)
      vWish.addWidget(lblWishText)

      # #remove
      vRemoveWidget = QWidget(self) #vertical layout to store item info
      vRemove = QVBoxLayout(vRemoveWidget)
      vRemove.setAlignment(Qt.AlignCenter)
      hRightButtons.addWidget(vRemoveWidget)

      lblBin = QLabel(self)                           #Remove Icon
      lblBin.setPixmap(QPixmap(BIN))
      lblBin.mousePressEvent = removeItem
      lblBin.setAlignment(Qt.AlignHCenter)
      lblBin.setCursor(Qt.PointingHandCursor)
      vRemove.addWidget(lblBin)

      lblRemoveText = QLabel("Remove", self)       #Remove text
      lblRemoveText.setFont(QFont('AnyStyle', 12))
      lblRemoveText.setAlignment(Qt.AlignHCenter)
      lblRemoveText.mousePressEvent = removeItem
      lblRemoveText.setCursor(Qt.PointingHandCursor)
      vRemove.addWidget(lblRemoveText)

#-------------------------------------------------------------------------------------Start Program
ex = MainWindow() #create MainWindow object
def createMain():
   app = QApplication(sys.argv)          
   ex.showMaximized()
   sys.exit(app.exec_())