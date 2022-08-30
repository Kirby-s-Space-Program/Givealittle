from collections import UserList
import sqlite3
from multiprocessing import connection
from sys import flags
from encrypter import encrypt

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
    salt=getSalt(email)
    snhpassword = encrypt(password, salt=salt)
    try:
        cursor.execute("SELECT Password FROM Users WHERE Email = ?", (email,))
        pas = cursor.fetchall()[0][0]
        if (pas == snhpassword): #attempt make sure password is matching
            return 0
        else:
            return 1
    except:
        return -1
        #return 0 if login success, 1 if details entered were incorrect and -1 if external error

#============================================================================================

def getInfo(email): #jsut takes in email and returns a list containing the users information in order name,surname,email,password
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
    UserList = cursor.fetchall()[0]

    return UserList
    

#============================================================================================

def getSalt(email): #Gets salt to compare passwords
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Salt FROM Users WHERE Email = ?", (email,))
        #cursor.execute("UPDATE Users SET Salt= 'de0b36567fca446c863f9c3d78162b11', Password= '14bfa65071cd794b5203284be0e048511169a20caa6e375b4791e2cce8d000f2ec1891b53a2288e32cea64dd2ebfb4cce487f9463a4e98ce1f488e9c58131401' WHERE Email='test@mail.com';")
        #connection.commit()
        salt = cursor.fetchall()[0][0]
        return salt
    except:
        print("There was an external error")
        return -1