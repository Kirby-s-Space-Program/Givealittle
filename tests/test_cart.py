from tabnanny import check
import unittest
from cart import *

testCart = currCart()
testWish = currWishList()

class DatabaseTest(unittest.TestCase):
    
    #adding to cart works
    def test_AddCart_success(self):
        check = testCart.add_item(0, "abc", 1)
        self.assertEqual(check, 0, "Should throw error code 0")
    #removing from cart works   
    def test_DelCart_Success(self):
        x = testCart.add_item(0, "abc", 0)
        check = testCart.remove_item(0)
        self.assertEqual(check, 0, "Should throw error code 0")
        
    #adding to cart works
    def test_AddWL_success(self):
        check = testWish.add_item(0, "abc", 1)
        self.assertEqual(check, 0, "Should throw error code 0")
    #removing from cart works   
    def test_DelWL_Success(self):
        x = testWish.add_item(0, "abc", 0)
        check = testWish.remove_item(0)
        self.assertEqual(check, 0, "Should throw error code 0")
    
        
        