import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = db.cursor()

# sql = "DROP TABLE costumer"
sql = "DROP TABLE IF EXISTS costumer"

mycursor.execute(sql)