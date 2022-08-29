import database

class currUser:
    def __init__(self, email): #this is called after users login has been verified
        userInfo = database.getInfo(email)
        self.email = email
        self.fName = userInfo[0]
        self.surname = userInfo[1]
        self.password = userInfo[3]
        self.Inventory = [] #this will later be use to store the items the user is selling
