import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

## Initial Connection
connection = mysql.connector.connect(host='localhost',
                                         database='enlightened dreamer',
                                         user='root')

cursor = connection.cursor()

class main_login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login_creds(self):
        # Checks if user is in Database
        user_permissions = "SELECT IF(EXISTS (SELECT * FROM users WHERE Username = ('%s')"\
                            "AND aes_decrypt(Password, 'PASS') = ('%s')),'True','False') AS result" % (self.username, self.password) 
        
        cursor.execute(user_permissions)
        user_data = cursor.fetchall()
          
        for user in user_data:
            response = user[0]
        
        if response == "True":
            return True
        else:
            return False
   

