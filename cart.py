from database import categoryList


class currCart:
    def __init__(self):
        self.cartList = {} #list of cart items in a dictionary with their price. Eg: cartlist["sword"] = 420.10
        self.totalCost = 0 #total sum of the price of items within the disctionary
        
    #add item usng its ID price and naem
    def add_item(self, itemID, itemName, itemPrice):
        try:   
            self.cartList[itemID] = [itemName, itemPrice]
            self.calc_total()
            return 0
        except:
            return 1
    #remove item usng its ID
    def remove_item(self, itemID):
        try:
            del self.cartList[itemID]
            self.calc_total()
            return 0
        except:
            return 1
    #keep track of the sum of the users cart when theyre using the application, its updated everytime they add or remove an item automatically  
    def calc_total(self):
        sum = 0
        try:
            for x in self.cartList:
                sum += self.cartList[x][1]
            self.totalCost = sum
            return 0
        except:
            return 1

class currWishList:
    def __init__(self):
        self.wishlist = {} #list of cart items in a dictionary with their price. Eg: cartlist["sword"] = 420.10
    #add item usng its ID price and naem    
    def add_item(self, itemID, itemName, itemPrice):
        try:
            self.wishlist[itemID] = [itemName, itemPrice]
            return 0
        except:
            return 1
    #remove item usng its ID
    def remove_item(self, itemID):
        try:
            del self.wishlist[itemID]
            return 0
        except:
            return 1