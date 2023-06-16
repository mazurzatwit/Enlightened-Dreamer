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

        self.username_text = self.findChild(QLineEdit, "username_textbox")
        self.password_text = self.findChild(QLineEdit, "password_textbox")

        self.login_button = self.findChild(QPushButton, "login_button")
        self.login_button.clicked.connect(self.save_text)

        #self.save_text()

    def save_text(self):
        username_text = self.username_text.text()
        password_text = self.password_text.text()

        eventInfo = [username_text, password_text]
        print(eventInfo)

        #print(username_text, password_text)