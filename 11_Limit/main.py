import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM costumer LIMIT 2")

result = mycursor.fetchall()

for x in result:
	print(x)