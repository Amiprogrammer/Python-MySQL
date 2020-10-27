import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM estudent WHERE name = %s"
val = ("juliao martins",)

mycursor.execute(sql,val)

result = mycursor.fetchone()

for x in result:
    print(x)
