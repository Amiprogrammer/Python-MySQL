import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM estudent")
mycursor.execute("SELECT id,name,address FROM estudent")

result = mycursor.fetchall()

for x in result:
    print(x)
