import sys
from Window import *

def main():
   app = QApplication(sys.argv)
   ex = MainWindow()                    #create MainWindow object
   ex.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    main()