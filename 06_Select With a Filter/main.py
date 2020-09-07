import mysql.connector

jmdb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = jmdb.cursor()

sql = "SELECT * FROM costumer WHERE name = %s"
val = ("berjeki",)

mycursor.execute(sql,val)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)