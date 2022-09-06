# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 890)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #------------------------------------------------------------
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(40, 130, 781, 41))
        self.Search.setObjectName("Search")
        self.SearchBut = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBut.setGeometry(QtCore.QRect(830, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SearchBut.setFont(font)
        self.SearchBut.setObjectName("SearchBut")
        #------------------------------------------------------------
        self.listCat = QtWidgets.QListWidget(self.centralwidget)
        self.listCat.setGeometry(QtCore.QRect(10, 280, 181, 541))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.listCat.setFont(font)
        self.listCat.setObjectName("listCat")
        self.lDeal = QtWidgets.QLabel(self.centralwidget)
        self.lDeal.setGeometry(QtCore.QRect(360, 180, 661, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.lDeal.setFont(font)
        self.lDeal.setObjectName("lDeal")
        self.textItems = QtWidgets.QTextBrowser(self.centralwidget)
        self.textItems.setGeometry(QtCore.QRect(230, 280, 841, 551))
        self.textItems.setObjectName("textItems")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "KIRBY MARKET"))
        self.SearchBut.setText(_translate("MainWindow", "Search"))
        self.lDeal.setText(_translate("MainWindow", "DEALS"))
        self.label.setText(_translate("MainWindow", "Shop by department"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.menuWish_List.setTitle(_translate("MainWindow", "Wish List"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSell.setTitle(_translate("MainWindow", "Sell"))
        self.menuCart.setTitle(_translate("MainWindow", "Cart"))
        self.actionInformation.setText(_translate("MainWindow", "Details"))
        self.actionTrack_Order.setText(_translate("MainWindow", "Track Order"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))

class UI(Ui_MainWindow):
     def __init__(self):
        super(UI, self).__init__()
        self.show()


def main():
   app = QApplication(sys.argv)
   ex = UI() 
   ex.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    main()