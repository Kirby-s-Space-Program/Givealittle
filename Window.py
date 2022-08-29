import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QWidget):
   def __init__(self):
      super().__inti__()_

      self.title = "Window"
      self.left = 500
      self.top = 200
      self.width = 300
      self.height = 250

      self.InitUI()

   def InitUI(self) :
      self.setWindowTitle (self. title)
      self.setWindowIcon (QtGui QIcon (self.iconName))
      self.setGeometry (self.left, self.top, self. width, self.height)

      vbox = QVBoxLayout ()
      self.btn = QPushButton ("Open Second Dialog")
      self.btn. setFont (QtGui.QFont ("Sanserif", 15) )
      vbox.addWidget (self.btn)
      self.setLayout (vbox)

      self.show ()



class Ui_Dialog(object):
   def setupUi(self, Dialog):
      Dialog.setObjectName("Dialog")
      Dialog.resize(1120, 840)
      Dialog.setAutoFillBackground(False)
      self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
      self.horizontalLayoutWidget.setGeometry(QtCore.QRect(730, 0, 391, 51))
      self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
      self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
      self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
      self.horizontalLayout.setSpacing(20)
      self.horizontalLayout.setObjectName("horizontalLayout")
      self.btnLogin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
      self.btnLogin.setObjectName("btnLogin")
      self.horizontalLayout.addWidget(self.btnLogin)
      self.btnLogin.clicked.connect(btnLogin_clicked)
      self.btnRegister = QtWidgets.QPushButton(self.horizontalLayoutWidget)
      self.btnRegister.setObjectName("btnRegister")
      self.horizontalLayout.addWidget(self.btnRegister)
      self.btnRegister.clicked.connect(btnRegister_clicked)

      self.retranslateUi(Dialog)
      QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
      _translate = QtCore.QCoreApplication.translate
      self.btnLogin.setText(_translate("Dialog", "Login"))
      self.btnRegister.setText(_translate("Dialog", "Register"))

def btnLogin_clicked():
   print ("Button login clicked")

def btnRegister_clicked():
   print ("Button register clicked")