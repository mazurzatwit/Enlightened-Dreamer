## Enlightened Dreamer will help our users delve deeper into their dreams and 
## sleep patterns. By tracking sleep patterns, users are able to analyze what 
## their dreams mean and how they might relate to their current state of mind. 
## The project consists of a web application supported by a backend that controls
## all user interaction. This user interaction includes recording dreams, a web 
## connection, and collects data on the user’s sleep patterns to be stored in a 
## secondary storage. The data will be displayed by a GUI via the use of the backend. 

##  python3 -m pip install mysql-connector-python
import sys
import typing
from PyQt5.QtWidgets import QStackedWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import login
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


#class save_login(QMainWindow):
     
    #def __init__(self):
     #    super().__init__()
      #   self.save_login = login.login_page()
         #self.save_login()
      
class main_window(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("UI/Home.ui", self)

          self.ui_stack = self.findChild(QStackedWidget, "stackedWidget")
          self.home = self.findChild(QWidget, "home_page")
          self.login_page = self.findChild(QWidget, "login_page")
          self.sign_up_page = self.findChild(QWidget, "sign_up_page")

          self.ui_stack.setCurrentWidget(self.home)
          
          #home page buttons
          self.sign_up_button = self.findChild(QPushButton, "sign_up_button")
          self.login_button = self.findChild(QPushButton, "login_button")
          self.sign_up_button.clicked.connect(self.show_sign_up_page)
          self.login_button.clicked.connect(self.show_login_page)
          
          #login page button
          self.login_btn = self.findChild(QPushButton, "login_btn")
          self.login_btn.clicked.connect(self.login_save_click)
          

          #sign up page button
          self.submit_button = self.findChild(QPushButton, "submit_button")

          #UI show
          #self.show()

     def login_save_click(self):
          self.save_login = login.login_page()

     def show_sign_up_page(self):
          self.ui_stack.setCurrentWidget(self.sign_up_page)

     def show_login_page(self):
          self.ui_stack.setCurrentWidget(self.login_page)


def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    window.setWindowTitle("Enlightened Dreamer")
    sys.exit(app.exec_()) 
main()


