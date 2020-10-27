import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root",
)

print(db)
