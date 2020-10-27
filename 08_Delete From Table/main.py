import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

# mycursor.execute("DELETE FROM estudent WHERE address = 'lahane'")

sql = "DELETE FROM estudent WHERE name = %s"
val = ("juliao martins",)

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted!")
