import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

class sign_up_page(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("UI/sign_up_page.ui", self)
        self.show()

       
    def show_sign_up(self):
        #loading sign up UI
            uic.loadUi("UI/sign_up_page.ui", self)

            #sign up information for new user
            #self.name = self.findChild(QLineEdit, "name_textbox")
            #self.email = self.findChild(QLineEdit, "email_textbox")
            #self.uname = self.findChild(QLineEdit, "username_textbox")
            #self.pword = self.findChild(QLineEdit, "password_textbox")
            
            #self.submit = self.findChild(QPushButton, "submit")
            #self.submit.clicked.connect(self.sign_up_info)

    def sign_up_info(self):
        name_text = self.name.text()
        email_text = self.email.text()
        uname_text = self.uname.text()
        pword_text = self.pword.text()

        new_user_info = [name_text, email_text, uname_text, pword_text]
        print(new_user_info)