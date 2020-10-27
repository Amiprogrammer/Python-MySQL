import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root",
        database="testing"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testing")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
