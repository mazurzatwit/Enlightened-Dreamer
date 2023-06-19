import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

class login_page(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("UI/Home.ui", self)

        #login username and password
        self.ui_stack = self.findChild(QStackedWidget, "stackedWidget")
        self.login_page = self.findChild(QWidget, "login_page")

        #finds text
        self.login_btn = self.findChild(QPushButton, "login_btn")
        self.username_text = self.findChild(QLineEdit, "username_textbox")
        self.password_text = self.findChild(QLineEdit, "password_textbox")
        #print(self.username_text.text())

        #self.login_btn.clicked.connect(self.save_text)

        self.save_text()


    def save_text(self):
        username_text = self.username_text.text()
        password_text = self.password_text.text()

        login_info = [username_text, password_text]
        print(login_info)

        #print(username_text, password_text)

