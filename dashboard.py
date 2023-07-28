import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

## Initial Connection
connection = mysql.connector.connect(host='localhost',
                                         database='enlightened dreamer',
                                         user='root')

cursor = connection.cursor()

class dashboard_view:
     
    def __init__(self, sleep_time, wake_time, dream_type, dream, date, username):
        self.sleep_time = sleep_time
        self.wake_time = wake_time
        self.dream_type = dream_type
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

         save_dream = "INSERT INTO Data SELECT ('%s'), ('%s'), ('%s'), ('%s'), ('%s'), ('%s')" % (self.sleep_time, self.wake_time, self.dream_type, self.dream, self.date, id)

         cursor.execute(save_dream)
         connection.commit()
          

    def dream_records(self):
        results = ""
        get_user_id = "SELECT User_ID FROM USERS WHERE Username = ('%s')" % (self.username)
        cursor.execute(get_user_id)
        user_id = cursor.fetchall()
        for user in user_id:
            id = user[0]

        curr_date = date.today()
        past_date = curr_date - timedelta(days = 7)
        get_dreams = "SELECT CONCAT (Date, ' - ', DreamType, ' - ',Dream) AS UserEntry FROM data WHERE User_ID = ('%s') AND Date BETWEEN ('%s') AND ('%s')" % (id, past_date.isoformat(), curr_date.isoformat())
        cursor.execute(get_dreams)
        dreams_of_week = cursor.fetchall()
        results = "   Date   -   Dream Type   -    Description    "
        for dream in dreams_of_week:
            for element in dream:
                results = results + "\n\n" + element
       
        return results
    
    def dream_analytics(self):
        results = ""
        get_user_id = "SELECT User_ID FROM USERS WHERE Username = ('%s')" % (self.username)
        cursor.execute(get_user_id)
        user_id = cursor.fetchall()
        for user in user_id:
            id = user[0]

        curr_date = date.today()
        past_date = curr_date - timedelta(days = 7)

        #get_analytics = """SELECT DreamType, CONCAT(FLOOR(ABS(TIME_TO_SEC(TIMEDIFF(STR_TO_DATE(CONCAT(Sleeptime, ' AM'), '%%h:%%i %%p'), STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p')))) / 3600), '.',MOD(FLOOR(ABS(TIME_TO_SEC(TIMEDIFF(STR_TO_DATE(CONCAT(Sleeptime, ' AM'), '%%h:%%i %%p'), STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p')))) / 60),60 ) ) AS time_in_between FROM data WHERE User_ID = ('%s') AND Date BETWEEN ('%s') AND ('%s')""" % (id, past_date.isoformat(), curr_date.isoformat())
        get_analytics = """SELECT DreamType, CONCAT(FLOOR( ABS(TIME_TO_SEC(TIMEDIFF(CASE WHEN STR_TO_DATE(Sleeptime, '%%h:%%i %%p') > STR_TO_DATE(Waketime, '%%h:%%i %%p') THEN STR_TO_DATE(CONCAT(Sleeptime, ' PM'), '%%h:%%i %%p') ELSE STR_TO_DATE(CONCAT(Sleeptime, ' AM'), '%%h:%%i %%p') END, CASE WHEN STR_TO_DATE(Sleeptime, '%%h:%%i %%p') > STR_TO_DATE(Waketime, '%%h:%%i %%p') THEN STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p') + INTERVAL 1 DAY ELSE STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p') END))) / 3600),'.', MOD(FLOOR(ABS(TIME_TO_SEC(TIMEDIFF(CASE WHEN STR_TO_DATE(Sleeptime, '%%h:%%i %%p') > STR_TO_DATE(Waketime, '%%h:%%i %%p') THEN STR_TO_DATE(CONCAT(Sleeptime, ' PM'), '%%h:%%i %%p') ELSE STR_TO_DATE(CONCAT(Sleeptime, ' AM'), '%%h:%%i %%p') END,CASE WHEN STR_TO_DATE(Sleeptime, '%%h:%%i %%p') > STR_TO_DATE(Waketime, '%%h:%%i %%p') THEN STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p') + INTERVAL 1 DAY ELSE STR_TO_DATE(CONCAT(Waketime, ' AM'), '%%h:%%i %%p') END))) / 60),60)) AS time_in_between FROM data WHERE User_ID = ('%s') AND Date BETWEEN ('%s') AND ('%s')""" % (id, past_date.isoformat(), curr_date.isoformat())


        # x axis values

        x = []

        # corresponding y axis values

        y = []

        cursor.execute(get_analytics)
        analytics_of_week = cursor.fetchall()
        for point in analytics_of_week:
            x.append(str(point[0]))
            if str(point[1]) == "None":
                y.append(float(0)) 
            else:
                y.append(float(point[1]))


        # plotting the points

        plt.scatter(x, y, label= "stars", color= "purple", marker= "*", s=100)


        # setting x and y axis range

        plt.ylim(0,18)

        plt.xlim(-1, len(x))


        # naming the x axis

        plt.xlabel('Dream Type')

        # naming the y axis

        plt.ylabel('Sleep Time (Hours)')

        # giving a title to my graph

        plt.title('Dream Type vs. Hours Slept')

        plt.xticks(rotation=45, ha='right')
        plt.yticks(range(0, 19, 1))

        plt.tight_layout()
        plt.savefig("Graph/graph_image.png")
        #plt.show()
                