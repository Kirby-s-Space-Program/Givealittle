import database
from cart import *

class currUser:
    def __init__(self, **kwargs): #this is called after users login has been verified
        self.email = kwargs.get('email', 0)
        if(self.email!=0):
            userInfo = database.getUserInfo(self.email)
            self.fName = userInfo[0]
            self.surname = userInfo[1]
            self.password = userInfo[3]
            self.Inventory = [] #this will later be use to store the items the user is selling
            self.cart = myCart #users cart
        
    def get_Name(self):
        return self.fName

myuser=currUser()