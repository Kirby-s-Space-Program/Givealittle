import sys
from Subwindows2 import *

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   ex.addButton()
   ex.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    main()