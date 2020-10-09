import mysql.connector

# connection to database server
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mysql_training"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE estudent (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), gender CHAR(1), address VARCHAR(250))")

sql = "INSERT INTO estudent (name,gender,address) VALUES (%s,%s,%s)"
val = [
    ("joao nunes","m","becora"),
    ("sebastiao soares","m","balide"),
    ("mariana tavares","f","matadoru"),
    ("celestino alves","m","quintal-kiik"),
    ("helena martins","f","tibar")
]

mycursor.executemany(sql,val)

if( mycursor.rowcount > 0 ):
    print(mycursor.rowcount, "inserted record(s)!")
else:
    print("insert failled!")
