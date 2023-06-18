## Enlightened Dreamer will help our users delve deeper into their dreams and 
## sleep patterns. By tracking sleep patterns, users are able to analyze what 
## their dreams mean and how they might relate to their current state of mind. 
## The project consists of a web application supported by a backend that controls
## all user interaction. This user interaction includes recording dreams, a web 
## connection, and collects data on the user’s sleep patterns to be stored in a 
## secondary storage. The data will be displayed by a GUI via the use of the backend. 

##  python3 -m pip install mysql-connector-python
import sys
from PyQt5.QtWidgets import QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from login import login_page
from sign_up import sign_up_page
import mysql.connector

## Initial Connection
connection = mysql.connector.connect(host='localhost',
                                         database='enlightened dreamer',
                                         user='root')

## Checks SQL connection
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record[0])

    username = 'Elle'
    password = 'L0nd0nGirl'

    user_permissions = "SELECT * FROM USERS WHERE Username = ('%s') AND aes_decrypt(Password, 'PASS') = ('%s')" % (username, password)
    cursor = connection.cursor()
    cursor.execute(user_permissions)
    # get all records
    user_data = cursor.fetchall()

    for user in user_data:
        print("Welcome", user[3])

      
class main_window(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("UI/login.ui", self)

          self.ui_stack = QStackedWidget()
          self.login = login_page()
          self.ui_stack.addWidget(self.login) #index 0
          self.sign_up = sign_up_page()
          self.ui_stack.addWidget(self.sign_up) #index 1

          #loading login UI
          
          #login_button = self.findChild(QPushButton, "login_button")
          
          self.sign_up_button = self.findChild(QPushButton, "sign_up")

          self.sign_up_button.clicked.connect(self.create_sign_up)


          
          #login_button.clicked.connect(self.login.save_text)

          #UI show
          self.show()

     def create_sign_up(self):
        self.ui_stack.setCurrentIndex(1)

    
        

def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.setWindowTitle("Enlightened Dreamer")
    sys.exit(app.exec_()) 
main()


