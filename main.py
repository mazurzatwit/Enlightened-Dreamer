## Enlightened Dreamer will help our users delve deeper into their dreams and 
## sleep patterns. By tracking sleep patterns, users are able to analyze what 
## their dreams mean and how they might relate to their current state of mind. 
## The project consists of a web application supported by a backend that controls
## all user interaction. This user interaction includes recording dreams, a web 
## connection, and collects data on the user’s sleep patterns to be stored in a 
## secondary storage. The data will be displayed by a GUI via the use of the backend. 

##  python3 -m pip install mysql-connector-python
import mysql.connector

print( "Let's Code a Project Ladies :))) ")

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

    user_permissions = "SELECT * FROM USERS WHERE Username = 'Elle' AND aes_decrypt(Password, 'PASS') = 'L0nd0nGirl';"
    cursor = connection.cursor()
    cursor.execute(user_permissions)
    # get all records
    user_data = cursor.fetchall()

    for user in user_data:
        print("Welcome", user[3])