# Install MySQL on your computer
# pip install mysql
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'dahkaso120',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE lhudata")

print("Database created successfully")

