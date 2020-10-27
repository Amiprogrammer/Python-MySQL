import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM estudent WHERE address = 'lahane'")

mydb.commit()

print(mycursor.rowcount, "record(s) deleted!")
