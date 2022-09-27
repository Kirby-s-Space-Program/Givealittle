import unittest
from database import *

class DatabaseTest(unittest.TestCase):
    def test_Register_success(self):
        check = register("name", "surname", "email", "password", "salt")
        self.assertEqual(check, 0, "Should throw error code 0")
    def test_Register_fail(self):
        check = register("name", "surname", "reg@mail.com", "password", "salt")
        self.assertEqual(check, 1, "Should throw error code 1")

    def test_Login_success(self):
        check = login("reg@mail.com", "1234")
        self.assertEqual(check, 0, "Should throw error code 0")  
    def test_Login_FailMismatch(self):
        check = login("reg@mail.com", "123")
        self.assertEqual(check, 1, "Should throw error code 1")
    
    def test_getInfo(self):
        check = getUserInfo("reg@mail.com")
        self.assertEqual(check, ('register', 
        'tests', 'reg@mail.com', 
        '4cdacfddbf05f958ad6d93740ac38116d36018da3f15245ed066ee31f658b72de49401e320d3476873217b451324c60aea539ccbee447f3ab66f50ef2cc06bab', 
        '37fa8e0cad5040bdb78f49ef773592fa'), "Should wrong info given")
    def test_getInfoNull(self):
        check = getUserInfo("")
        self.assertEqual(check, "User does not exist", "Should wrong info given")

    def test_getSalt(self):
        check = getSalt("reg@mail.com")
        self.assertEqual(check, '37fa8e0cad5040bdb78f49ef773592fa', "Should wrong info given")
    def test_getSaltNull(self):
        check = getSalt("")
        self.assertEqual(check, -1, "Should wrong info given")

    def test_addProduct(self):
        check = addProduct("Infinity Edge", 0, "ProductEmail", "productCat", "productPAth")
        self.assertEqual(check, 0, "should throw code 0")
    #def test_addProductFail(self):
        #check = addProduct("Infinity Edge", "ProductPrice", "ProductEmail")
        #self.assertEqual(check, 0, "show throw code 0")


