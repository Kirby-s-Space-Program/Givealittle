import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QWidget):
    def __init__(self):
        super ().__init__()

        self.title = "Window"
        self.left = 800
        self.top = 300
        self.width = 300
        self.height = 250

        self.InitUI()

    def InitUI(self) :
        self.setWindowTitle (self. title)
        self.setGeometry (self.left, self.top, self. width, self.height)
        self.vbox = QVBoxLayout()
        self.setLayout (self.vbox)

class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.title = "Give-a-Little"
        self.left = 250
        self.top = 250
        self.width = 1000
        self.height = 1000

        self.InitUI()
        self.addLoginButtons()
        self.show()

    def addLoginButtons(self):
        self.hLayoutWidget = QWidget(self)
        self.hLayoutWidget.setGeometry(QtCore.QRect(600, 0, 400, 50))
        self.hLayoutWidget.setObjectName("hLayoutWidget")
        self.hLayout = QHBoxLayout(self.hLayoutWidget)
        self.hLayout.setContentsMargins(20, 0, 20, 0)
        self.hLayout.setSpacing(20)
        self.hLayout.setObjectName("hLayout")
        self.vbox.addWidget(self.hLayoutWidget)

        self.btnLogin = QPushButton(self.hLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setText("Login")
        self.btnLogin.clicked.connect(self.btnLogin_clicked)
        self.hLayout.addWidget(self.btnLogin)

        self.btnRegister = QtWidgets.QPushButton(self.hLayoutWidget)
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.setText("Register")
        self.btnRegister.clicked.connect(self.btnRegister_clicked)
        self.hLayout.addWidget(self.btnRegister)

    def btnLogin_clicked(self):
        self.mydialog = Window()
        self.mydialog.show()

    def btnRegister_clicked(self):
        self.mydialog = Window()
        self.mydialog.show()