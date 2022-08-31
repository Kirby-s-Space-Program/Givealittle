import hashlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *
from database import register, login
from user import *
from encrypter import *

logged = 2 #-1=external error, 0=logged in, 1=wrong details, 2=have not tried
user=currUser()
#-------------------------------------------------------------------------------------Base Class Window
class Window(QWidget):  
   def __init__(self):
      super ().__init__()

      self.title = "Window" #define window attributes
      self.left = LEFT_SUB
      self.top = TOP_SUB
      self.width = WIDTH_SUB
      self.height = HEIGHT_SUB

      self.vbox = QVBoxLayout()
      self.vbox.setContentsMargins(MARGIN_SUB_VBOX, TOP_SUB_VBOX, MARGIN_SUB_VBOX, TOP_SUB_VBOX) 
      self.setLayout(self.vbox)

      self.InitUI()

   def InitUI(self) :  #set window attributes
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self. width, self.height)
      self.setWindowIcon(QIcon("logo.png"))

#-----------------------------------------------------------------------------------------Subclass MainWindow
class MainWindow(Window): 
   def __init__(self):
      super().__init__()

      self.title = "Give-a-Little" #define window attributes
      self.left = 0
      self.top = 0
      self.width = WIDTH_MAIN
      self.height = HEIGHT_MAIN

      self.InitUI()
      self.addLoginButtons()
      self.showMaximized()
      self.show()

   def addLoginButtons(self):               #Add login/register buttons
      self.hLayoutWidget = QWidget(self)
      self.hLayoutWidget.setGeometry(QRect(HLAYOUT_LEFT, HLAYOUT_TOP, HLAYOUT_WIDTH, HLAYOUT_HEIGHT))
      self.hLayoutWidget.setObjectName("hLayoutWidget")
      self.hLayout = QHBoxLayout(self.hLayoutWidget)
      self.hLayout.setSpacing(HLAYOUT_SPACING)
      self.hLayout.setObjectName("hLayout")

      self.btnLogin = QPushButton(self.hLayoutWidget) #Login Button
      self.btnLogin.setObjectName("btnLogin")
      self.btnLogin.setText("Login")
      self.btnLogin.clicked.connect(self.btnLogin_clicked)
      self.hLayout.addWidget(self.btnLogin)

      self.btnRegister = QPushButton(self.hLayoutWidget) #Register button
      self.btnRegister.setObjectName("btnRegister")
      self.btnRegister.setText("Register")
      self.btnRegister.clicked.connect(self.btnRegister_clicked)
      self.hLayout.addWidget(self.btnRegister)

   def btnLogin_clicked(self): #Open new Window when login button pressed
      self.mydialog = LoginWindow()
      self.mydialog.show()

   def btnRegister_clicked(self): #Open new Window when register button pressed
      self.mydialog = RegisterWindow()
      self.mydialog.show()

#----------------------------------------------------------------------------------------------Subclass LoginWindow
class LoginWindow(Window): 
   def __init__(self):
      super().__init__()

      self.title = "Login"

      self.InitUI()
      self.addLoginWidgets()
   
   def addLoginWidgets(self):
      self.lblLoginHeader = QLabel('Login', self)             #Login label
      self.lblLoginHeader.setFont(QFont('AnyStyle', 25))
      self.vbox.addWidget(self.lblLoginHeader)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.vboxEmailWidget = QWidget(self)                    #Email
      self.vboxEmailWidget.setObjectName("vboxEmailWidget")
      self.vboxEmail = QVBoxLayout(self.vboxEmailWidget)
      self.vboxEmail.setObjectName("vboxEmail")
      self.vbox.addWidget(self.vboxEmailWidget)

      self.lblEmail= QLabel('Email', self.vboxEmailWidget)
      self.lblEmail.setFont(QFont('AnyStyle', 15))
      self.vboxEmail.addWidget(self.lblEmail)

      self.ledtEmail = QLineEdit(self.vboxEmailWidget)
      self.vboxEmail.addWidget(self.ledtEmail)

      self.vboxPassWidget = QWidget(self)                    #Password
      self.vboxPassWidget.setObjectName("vboxPassWidget")
      self.vboxPass = QVBoxLayout(self.vboxPassWidget)
      self.vboxPass.setObjectName("vboxPass")
      self.vbox.addWidget(self.vboxPassWidget)

      self.lblPass= QLabel('Password', self.vboxPassWidget)
      self.lblPass.setFont(QFont('AnyStyle', 15))
      self.vboxPass.addWidget(self.lblPass)

      self.ledtPass = QLineEdit(self.vboxPassWidget)
      self.ledtPass.setEchoMode(QLineEdit.Password)
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
      self.btnLogin.clicked.connect(self.btnLogin_clicked)
      self.hbox.addWidget(self.btnLogin)

   def btnLogin_clicked(self): #check login details  TODO: check user login
      self.email = self.ledtEmail.text()
      self.password = self.ledtPass.text()
      logged = login(self.email, self.password)
      
      if(not logged):
         user = currUser(email=self.email)
         print("Login successful ", logged)
      elif(logged==1):
         print("Incorrect details", logged)
      elif(logged==-1):
         print("There was an external error", logged)
      
#----------------------------------------------------------------------------------------------Subclass RegisterWindow

class RegisterWindow(Window): 
   def __init__(self):
      super().__init__()

      self.title = "Register"

      self.InitUI()
      self.addRegisterWidgets()
   
   def addRegisterWidgets(self):
      self.lblRegisterHeader = QLabel('Register', self)             #Register label
      self.lblRegisterHeader.setFont(QFont('AnyStyle', 25))
      self.vbox.addWidget(self.lblRegisterHeader)

      self.vbox.addWidget(QLabel(self))                       #Space

      self.vboxFNameWidget = QWidget(self)                    #First Name
      self.vboxFNameWidget.setObjectName("vboxFNameWidget")
      self.vboxFName = QHBoxLayout(self.vboxFNameWidget)
      self.vboxFName.setObjectName("vboxFName")
      self.vbox.addWidget(self.vboxFNameWidget)

      self.lblFName= QLabel('First Name', self.vboxFNameWidget)
      self.lblFName.setFont(QFont('AnyStyle', 15))
      self.vboxFName.addWidget(self.lblFName)

      self.ledtFName = QLineEdit(self.vboxFNameWidget)
      self.vboxFName.addWidget(self.ledtFName)

      self.vboxEmailWidget = QWidget(self)                    #Email
      self.vboxEmailWidget.setObjectName("vboxEmailWidget")
      self.vboxEmail = QVBoxLayout(self.vboxEmailWidget)
      self.vboxEmail.setObjectName("vboxEmail")
      self.vbox.addWidget(self.vboxEmailWidget)

      self.lblEmail= QLabel('Email', self.vboxEmailWidget)
      self.lblEmail.setFont(QFont('AnyStyle', 15))
      self.vboxEmail.addWidget(self.lblEmail)

      self.ledtEmail = QLineEdit(self.vboxEmailWidget)
      self.vboxEmail.addWidget(self.ledtEmail)

      self.vboxPassWidget = QWidget(self)                    #Password
      self.vboxPassWidget.setObjectName("vboxPassWidget")
      self.vboxPass = QVBoxLayout(self.vboxPassWidget)
      self.vboxPass.setObjectName("vboxPass")
      self.vbox.addWidget(self.vboxPassWidget)

      self.lblPass= QLabel('Password', self.vboxPassWidget)
      self.lblPass.setFont(QFont('AnyStyle', 15))
      self.vboxPass.addWidget(self.lblPass)

      self.ledtPass = QLineEdit(self.vboxPassWidget)
      self.ledtPass.setEchoMode(QLineEdit.Password)
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
      self.btnLogin.clicked.connect(self.btnLogin_clicked)
      self.hbox.addWidget(self.btnLogin)

   def btnLogin_clicked(self): #check login details  TODO: check user login
      self.email = self.ledtEmail.text()
      self.password = self.ledtPass.text()
      logged = login(self.email, self.password)
      
      if(not logged):
         user = currUser(email=self.email)
         print("Login successful ", logged)
      elif(logged==1):
         print("Incorrect details", logged)
      elif(logged==-1):
         print("There was an external error", logged)