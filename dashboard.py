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

class dashboard_view:
     
    def __init__(self, sleep_time, wake_time, dream, date, username):
        self.sleep_time = sleep_time
        self.wake_time = wake_time
        self.dream = dream
        self.date = date
        self.username = username

    def dream_info_popup(self):
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Information)
        popup.setWindowTitle("Dream Catagories")
        popup.setText("No Dream: A dream did not occur.\n\n"\
                        "Normal Dream: Sequences of thoughts, images, or emotions that occur in a person’s mind while asleep.\n\n"\
                        "Daydream: a dream that occurs while the person is awake.\n\n"\
                        "Lucid Dream: A dream where the person in the dream is actively aware that they are dreaming.\n\n"\
                        "False Awakening: A dream that occurs when the sleeper thinks they are awake when in reality they are asleep.\n\n"\
                        "Nightmare: A frightening or creepy dream that causes the dreamer to awaken.\n\n")
        
        popup.exec()

    def save_new_dream(self):
         get_user_id = "SELECT User_ID FROM USERS WHERE Username = ('%s')" % (self.username)
         cursor.execute(get_user_id)
         user_id = cursor.fetchall()
         for user in user_id:
            id = user[0]

         print(id)

         save_dream = "INSERT INTO Data SELECT ('%s'), ('%s'), ('%s'), ('%s'), ('%s')" % (self.sleep_time, self.wake_time, self.dream, self.date, id)

         cursor.execute(save_dream)
         connection.commit()
          