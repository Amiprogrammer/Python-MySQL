import mysql.connector

# connection to database server
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mysql_traning") # create my database

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
