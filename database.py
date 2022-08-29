from collections import UserList
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
        return False
        
    connection.commit()
    return True
    #return True or registration success, false if there was an error
    

#============================================================================================

def login(email, password): #take in user info
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Password FROM Users WHERE Email = ?", (email,))
        if (cursor.fetchall()[0][0] == password): #attempt make sure password is matching
            connection.commit()
            return "Login"
        else:
            return "incorrect"
    except:
        print("error")
        return False
        #return Login if login success, incorrect if details entered were incorrect and False if external error

#============================================================================================

def getInfo(email): #jsut takes in email and returns a list containing the users information in order name,surname,email,password
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
    UserList = cursor.fetchall()[0]

    return UserList
    

