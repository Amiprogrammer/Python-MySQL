import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
	)

mycursor = db.cursor()

# mycursor.execute("SELECT * FROM costumer ORDER BY name") or "SELECT * FROM costumer ORDER BY name ASC"

mycursor.execute("SELECT * FROM costumer ORDER BY name DESC")

result = mycursor.fetchall()

for x in result:
	print(x)