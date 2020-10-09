import mysql.connector

# connection to database server
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mysql_training"
)

mycursor = mydb.cursor()

print("=== Databases Application ===")
