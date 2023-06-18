import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

class login_page(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("UI/login.ui", self)

        #login username and password
        self.username_text = self.findChild(QLineEdit, "username_textbox")
        self.password_text = self.findChild(QLineEdit, "password_textbox")

        self.login_button = self.findChild(QPushButton, "login_button")
        self.login_button.clicked.connect(self.save_text)

        self.sign_up_button = self.findChild(QPushButton, "sign_up")

        #self.save_text()

    def save_text(self):
        username_text = self.username_text.text()
        password_text = self.password_text.text()

        login_info = [username_text, password_text]
        print(login_info)

        #print(username_text, password_text)

