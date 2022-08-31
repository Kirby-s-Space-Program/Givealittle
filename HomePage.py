from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("HomePage.ui", self) #load the ui file
        
        #define widgets
        self.title = self.findChild(QLabel, "Title")
        self.search = self.findChild(QLineEdit, "Search")
        self.listCat = self.findChild(QListWidget, "listCat")
        
        #add items to widegt
        self.listCat.insertItem(0, "Beauty")
        self.listCat.insertItem(1, "Books")
        self.listCat.insertItem(2, "Clothes")
        self.listCat.insertItem(3, "Electronics")
        self.listCat.insertItem(4, "Gaming")
        self.listCat.insertItem(5, "EHome and Appliances")
        self.listCat.insertItem(6, "Sports")
        
        self.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
