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
import sign_up
import mysql.connector

## Initial Connection
connection = mysql.connector.connect(host='127.0.0.1',
                                         database='ed',
                                         user='AdminAccount',
                                         password='4r3y3s')

## Checks SQL connection
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record[0])

    # Test User Creds: 
    #username = 'Elle'
    #password = 'L0nd0nGirl'
      
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
          self.back_button = self.findChild(QPushButton, "back_button")
          self.username_text = self.findChild(QLineEdit, "username_textbox")
          self.password_text = self.findChild(QLineEdit, "password_textbox")
          self.login_btn.clicked.connect(self.login_save_click)
          self.back_button.clicked.connect(self.show_home_page)
          

          #sign up page button
          self.submit_button = self.findChild(QPushButton, "submit_button")
          self.back_btn = self.findChild(QPushButton, "back_btn")
          self.name_text = self.findChild(QLineEdit, "name_textbox")
          self.email_text = self.findChild(QLineEdit, "email_textbox")
          self.uname_text = self.findChild(QLineEdit, "uname_textbox")
          self.pass_text = self.findChild(QLineEdit, "pass_textbox")
          self.submit_button.clicked.connect(self.sign_up_save)
          self.back_btn.clicked.connect(self.show_home_page)

         
     def login_save_click(self):
          username_text = self.username_text.text()
          password_text = self.password_text.text()

          self.curr_login = login.main_login(username_text, password_text)
          self.curr_login.check_login_creds()

        
     def sign_up_save(self):
         name_text = self.name_text.text()
         email_text = self.email_text.text()
         uname_text = self.uname_text.text()
         pass_text = self.pass_text.text()

         self.new_user = sign_up.sign_up_page(name_text, email_text, uname_text, pass_text)
         self.new_user.save_new_user()

         self.name_text.clear()
         self.email_text.clear()
         self.uname_text.clear()
         self.pass_text.clear()


     def show_sign_up_page(self):
          self.ui_stack.setCurrentWidget(self.sign_up_page)

     def show_login_page(self):
          self.ui_stack.setCurrentWidget(self.login_page)

     def show_home_page(self):
          self.ui_stack.setCurrentWidget(self.home)
          self.name_text.clear()
          self.email_text.clear()
          self.uname_text.clear()
          self.pass_text.clear()
          self.username_text.clear()
          self.password_text.clear()



def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    window.setWindowTitle("Enlightened Dreamer")
    sys.exit(app.exec_()) 
main()


