import mysql.connector

jm = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
)

mycursor = jm.cursor()

sql = "INSERT INTO costumer (name,address) VALUES (%s,%s)"
val = ("Teresinha","Taibessi")

mycursor.execute(sql,val)

jm.commit()

print("1 record inserted, ID", mycursor.lastrowid)