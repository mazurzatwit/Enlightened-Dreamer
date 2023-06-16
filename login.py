import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

class login_page(QMainWindow):
    def __init__(self, main_instance):
        super(login_page, self).__init__()
        self.main_instance = main_instance
        uic.loadUi("UI/login.ui", self)

        #login username and password
        self.username_text = self.findChild(QLineEdit, "username_textbox")
        self.password_text = self.findChild(QLineEdit, "password_textbox")

        self.login_button = self.findChild(QPushButton, "login_button")
        self.login_button.clicked.connect(self.save_text)

        self.sign_up_button = self.findChild(QPushButton, "sign_up")
        self.sign_up_button.clicked.connect(self.show_sign_up)

        #self.save_text()

    def save_text(self):
        username_text = self.username_text.text()
        password_text = self.password_text.text()

        login_info = [username_text, password_text]
        print(login_info)

        #print(username_text, password_text)

    def show_sign_up(self):
        #loading sign up UI
        uic.loadUi("UI/sign_up_page.ui", self)

        #sign up information
        self.name = self.findChild(QLineEdit, "name_textbox")
        self.email = self.findChild(QLineEdit, "email_textbox")
        self.uname = self.findChild(QLineEdit, "username_textbox")
        self.pword = self.findChild(QLineEdit, "password_textbox")
        
        self.submit = self.findChild(QPushButton, "submit")
        self.submit.clicked.connect(self.sign_up_info)

    def sign_up_info(self):
        name_text = self.name.text()
        email_text = self.email.text()
        uname_text = self.uname.text()
        pword_text = self.pword.text()

        new_user_info = [name_text, email_text, uname_text, pword_text]
        print(new_user_info)