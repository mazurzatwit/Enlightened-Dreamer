## Enlightened Dreamer will help our users delve deeper into their dreams and 
## sleep patterns. By tracking sleep patterns, users are able to analyze what 
## their dreams mean and how they might relate to their current state of mind. 
## The project consists of a web application supported by a backend that controls
## all user interaction. This user interaction includes recording dreams, a web 
## connection, and collects data on the user’s sleep patterns to be stored in a 
## secondary storage. The data will be displayed by a GUI via the use of the backend. 

##  python3 -m pip install mysql-connector-python
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
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
          super(main_window, self).__init__()

          #loading login UI
          uic.loadUi("UI/login.ui", self)
          self.show()
          

def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.setWindowTitle("Enlightened Dreamer")
    sys.exit(app.exec_()) 
main()


