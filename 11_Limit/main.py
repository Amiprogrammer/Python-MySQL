import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

sql = "INSERT INTO estudent (name,email,address) VALUES (%s,%s,%s)"
val = [
    ("maia soares","maiasoares@gmail.com","tasi-3"),
    ("hernanda silva","hernasilva@gmail.com","becora"),
    ("silvia sousa","silviasou@gmail.com","bidau"),
    ("jaime de jesus","jaimedjesus@gmail.com","beto"),
    ("cinto cabral","cintocabral@gmail.com","lahane")
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted!")
