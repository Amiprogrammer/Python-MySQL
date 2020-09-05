"""
	to create new table from databases you need the "CREATE TABLE" statement

	example :
		"CREATE TABLE name (column1 (type), column2 (type))"

	to view your table use "SHOW TABLES"

"""
import mysql.connector

jmdb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
	)

mycursor = jmdb.cursor()

# mycursor.execute("CREATE TABLE costumer (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE costumer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("CREATE TABLE item (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for i in mycursor:
	print(i)