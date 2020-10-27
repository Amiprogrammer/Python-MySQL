import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

sql = "INSERT INTO estudent (name,email,address) VALUES (%s,%s,%s)"
val = ("juliao martins","juliaomartins@gmail.com","tasi-3")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted!")
