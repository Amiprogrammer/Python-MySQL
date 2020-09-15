import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = db.cursor()

# mycursor.execute("SELECT * FROM costumer LIMIT 3")
mycursor.execute("SELECT * FROM costumer LIMIT 5 OFFSET 2")

result = mycursor.fetchall()

for x in result:
	print(x)