import mysql.connector

jm = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
)

mycursor = jm.cursor()

mycursor.execute("SELECT * FROM costumer")

# myresult = mycursor.fetchall()
myresult = mycursor.fetchone()

for x in myresult:
	print(x)