import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testing")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
