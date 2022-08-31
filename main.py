import sys
from Window import *

def main():
   app = QApplication(sys.argv)
   ex = MainWindow()                    #create MainWindow object
   ex.showMaximized()
   sys.exit(app.exec_())

if __name__ == "__main__":
    main()