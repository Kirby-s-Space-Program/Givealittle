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

    def addButton(self):
        vbox = QVBoxLayout ()
        self.btn = QPushButton ("Open Second Dialog")
        self.btn. setFont (QtGui.QFont ("Sanserif", 15) )
        vbox.addWidget (self.btn)
        self.setLayout (vbox)


class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.title = "Give-a-Little"
        self.left = 250
        self.top = 250
        self.width = 1000
        self.height = 1000

        self.InitUI()

