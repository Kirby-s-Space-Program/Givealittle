from database import categoryList


class currCart:
    def __init__(self):
        self.cartList = {} #list of cart items in a dictionary with their price. Eg: cartlist["sword"] = 420.10
        self.totalCost = 0 #total sum of the price of items within the disctionary
        
    def add_item(self, itemID, itemName, itemPrice):
        self.cartList[itemID] = [itemName, itemPrice]
        self.calc_total()
       
    def calc_total(self):
        sum = 0
        
        for x in self.cartList:
            sum += self.cartList[x][1]
        self.totalCost = sum