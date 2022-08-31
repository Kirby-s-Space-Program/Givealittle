import unittest
from Window import *
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

class WindowTest(unittest.TestCase):
    app = QApplication(sys.argv)
    base_window = Window()
    # main_window = MainWindow()
    # login_window = LoginWindow()
    # register_window = RegisterWindow()

    #Checks window objects creation 
    def test_base_window_object_creation(self): 
        self.assertEqual(self.base_window.title, "Window", "Base Window object failed to be initialised")

    # def test_main_window_object_creation(self):
    #     self.assertEqual(self.main_window.title, "Kirby's Marketplace", "Main Window object failed to be initialised")

    # def test_login_window_object_creation(self):
    #     self.assertEqual(self.login_window.title, "Login", "Login Window object failed to be initialised")

    # def test_register_window_object_creation(self):
    #     self.assertEqual(self.register_window.title, "Register", "Register Window object failed to be initialised")

if __name__ == '__main__':
    unittest.main()