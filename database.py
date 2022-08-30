from collections import UserList
from os import remove
import sqlite3
from multiprocessing import connection
from sys import flags

connection = sqlite3.connect('KirbysDatabase.db')
#============================================================================================

def register(fname, surname, email, password):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", (fname, surname, email, password)) #attempt registration
    except:
        return 1
        
    connection.commit()
    return 0
    #return True or registration success, false if there was an error
    

#============================================================================================

def login(email, password): #take in user info
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Password FROM Users WHERE Email = ?", (email,))
        if (cursor.fetchall()[0][0] == password): #attempt make sure password is matching
            connection.commit()
            return 0
        else:
            return 1
    except:
        print("error")
        return -1
        #return Login if login success, incorrect if details entered were incorrect and False if external error

#============================================================================================

def getUserInfo(email): #jsut takes in email and returns a list containing the users information in order name,surname,email,password
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
    UserList = cursor.fetchall()[0]

    return UserList

#============================================================================================

def addProduct(ProductName, ProductPrice, ProductEmail): #adds a product to the database, auto increments and sets the ID
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Products (ProductName, ProductPrice, ProductOwner) VALUES (?, ?, ?)", (ProductName, ProductPrice, ProductEmail))
    except:
        return 1
        
    connection.commit()
    return 0

def removeProduct(productID): #removes item from the databse using only the ID since the ID is unique to each product
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Products WHERE ProductID = ?", (productID,))
    except:
        return 1
        
    connection.commit()
    return 0
