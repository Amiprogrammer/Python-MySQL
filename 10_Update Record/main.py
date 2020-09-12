import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE costumer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
	# print(x)

# sql = "INSERT INTO costumer (name,address) VALUES (%s,%s)"
# val = [
# 	("Rivaldo Li","Becora"),
# 	("Luduvina Castro","Lahane"),
# 	("Lurdes Baquita","Audian"),
# 	("Genilda Li","Perunas"),
# 	("Joaquim Gomes","Vilaverde")
# ]

# mycursor.executemany(sql,val)

# db.commit()

# print(mycursor.rowcount, "Inserted record(s).")

# mycursor.execute("UPDATE costumer SET address = \"Tasi3\" WHERE name = \"Genilda Li\"")

# db.commit()

# print(mycursor.rowcount, " record(s) affected.")

# mycursor.execute("SELECT * FROM costumer")

# result = mycursor.fetchall()

# for x in result:
	# print(x)

sql = "UPDATE costumer SET name = %s WHERE address = %s"
val = ("Teresinha Pinto","Lahane")

mycursor.execute(sql,val)

db.commit()

print(mycursor.rowcount, "record(s) affected.")