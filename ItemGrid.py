from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *

class itemGrid(QWidget):
    def __init__(self, parentWindow): #parentWidnow is the mainWindow object to be passed as a parameter 
      super ().__init__()
      self.parentWindow = parentWindow