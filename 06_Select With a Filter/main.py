import mysql.connector

jmdb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = jmdb.cursor()

mycursor.execute("SELECT * FROM costumer WHERE name LIKE \"%ohn%\"")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)