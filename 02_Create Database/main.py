"""
- now we use
	^ CREATE DATABASE mydatabase <to create my database>
	^ SHOW DATABASES <to show my databases>

"""
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj"
	)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE jmkodigu")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
	print(i)

# try to access mydatabases
jmdb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
	)

print(jmdb)