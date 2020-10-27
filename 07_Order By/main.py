import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM estudent ORDER BY name ASC")
mycursor.execute("SELECT * FROM estudent ORDER BY name DESC")

result = mycursor.fetchall()

for x in result:
    print(x)
