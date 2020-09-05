import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj"
	)

print(mydb)