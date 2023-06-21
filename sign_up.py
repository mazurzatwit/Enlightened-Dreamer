import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

#database connection
connection = mysql.connector.connect(host='localhost',
                                         database='ed',
                                         user='Zoe',
                                         password='4r3y3s')

cursor = connection.cursor()

class sign_up_page:
    
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def save_new_user (self):
         user_sign_up = "INSERT INTO Users (User_ID, Name, Email, Username, Password) SELECT * FROM (  SELECT IF(NOT EXISTS (SELECT * FROM Users WHERE User_ID = FLOOR(RAND() * 90000 + 10000)), FLOOR(RAND() * 90000 + 10000), NULL) AS User_ID, ('%s') AS Name, ('%s') AS Email, ('%s') AS Username, AES_ENCRYPT(('%s'), 'PASS') AS Password ) AS tmp" % (self.name, self.email, self.username, self.password)

         cursor.execute(user_sign_up)
         connection.commit()

         
       