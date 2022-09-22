import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *
from database import register, login
from user import *
from login.encrypter import encrypt
from login.verification import *

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

      self.font = QFont('Kirby Classic')
      self.font.setPointSize(50)

      self.labelColorEffect = QGraphicsColorizeEffect()
      self.labelColorEffect.setColor(PINK)
      self.labelShadowColorEffect = QGraphicsColorizeEffect()
      self.labelShadowColorEffect.setColor(DARK_PINK)

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

      self.left = 0
      self.top = 0
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
         self.menuWish_List = QAction('Wish List', self.menubar)
         self.menuWish_List.setObjectName("menuWish_List")
         self.menuWish_List.triggered.connect(self.btnTemp)
         self.menubar.addAction(self.menuWish_List)

         #Cart sub tabs
         self.menuCart = QAction('Cart', self.menubar)
         self.menuCart.setObjectName("menuCart")
         self.menuCart.triggered.connect(self.btnTemp)
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

      self.btnRegister = QPushButton(self.hboxWidget)            #Refgister Button
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
#-------------------------------------------------------------------------------------Start Program
def createMain():
   app = QApplication(sys.argv)          
   ex.showMaximized()
   sys.exit(app.exec_())
