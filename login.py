import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

#database connection
connection = mysql.connector.connect(host='10.220.32.138',
                                         database='ed',
                                         user='Zoe',
                                         password='4r3y3s')

cursor = connection.cursor()

class main_login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login_creds(self):
        # Checks if user is in Database
        user_permissions = "SELECT IF(Username = ('%s'), 'True', 'False') FROM users WHERE aes_decrypt(Password, 'PASS') = ('%s')" % (self.username, self.password)
        cursor.execute(user_permissions)
        user_data = cursor.fetchall()
          
        for user in user_data:
            print(user[0])    
   

