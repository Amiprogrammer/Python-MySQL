import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

sql = "UPDATE estudent SET name=%s WHERE address=%s"
val = ("antonio marcal","tibar")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) updated!")
