from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *

class Window(QWidget):  #Base Class Window
    def __init__(self):
        super ().__init__()

        self.title = "Window" #define window attributes
        self.left = 800
        self.top = 300
        self.width = 300
        self.height = 250

        self.InitUI()

    def InitUI(self) :  #set window attributes
        self.setWindowTitle (self.title)
        self.setGeometry (self.left, self.top, self. width, self.height)
        self.setWindowIcon(QIcon("logo.png"))
        self.vbox = QVBoxLayout()
        self.setLayout (self.vbox)

class MainWindow(Window): #Subclass MainWindow
    def __init__(self):
        super().__init__()

        self.title = "Give-a-Little" #define window attributes
        self.left = 0
        self.top = 0
        self.width = SIZE_WIDTH_MAIN
        self.height = SIZE_HEIGHT_MAIN

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
        self.vbox.addWidget(self.hLayoutWidget)

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
        self.mydialog = Window()
        self.mydialog.show()

    def btnRegister_clicked(self): #Open new Window when register button pressed
        self.mydialog = Window()
        self.mydialog.show()