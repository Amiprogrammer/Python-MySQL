import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="mydatabase"
)

mycursor = db.cursor()

# mycursor.execute("DELETE FROM costumer WHERE address = \"laulara\"")

sql = "DELETE FROM costumer WHERE name = %s"
val = ("ameta",)

mycursor.execute(sql,val)

db.commit()

print(mycursor.rowcount, "has deleled!")