from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *

class Window(QWidget):  #Base Class Window
   def __init__(self):
      super ().__init__()

      self.title = "Window" #define window attributes
      self.left = LEFT_SUB
      self.top = TOP_SUB
      self.width = WIDTH_SUB
      self.height = HEIGHT_SUB

      self.vbox = QVBoxLayout()
      self.vbox.setContentsMargins(LEFT_SUB_VBOX, TOP_SUB_VBOX, 0, TOP_SUB_VBOX)
      self.setLayout(self.vbox)

      self.InitUI()

   def InitUI(self) :  #set window attributes
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self. width, self.height)
      self.setWindowIcon(QIcon("logo.png"))

class MainWindow(Window): #Subclass MainWindow
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
      self.mydialog = Window()
      self.mydialog.show()

class LoginWindow(Window): #Subclass LoginWindow
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
      self.vboxEmail.setContentsMargins(0, 0, RIGHT_SUB_EDIT, 0)
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
      self.vboxPass.setContentsMargins(0, 0, RIGHT_SUB_EDIT, 0)
      self.vboxPass.setObjectName("vboxPass")
      self.vbox.addWidget(self.vboxPassWidget)

      self.lblPass= QLabel('Password', self.vboxPassWidget)
      self.lblPass.setFont(QFont('AnyStyle', 15))
      self.vboxPass.addWidget(self.lblPass)

      self.ledtPass = QLineEdit(self.vboxPassWidget)
      self.ledtPass.setEchoMode(QLineEdit.Password)
      self.vboxPass.addWidget(self.ledtPass)

      self.vbox.addWidget(QLabel(self))                       #Space