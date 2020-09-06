import mysql.connector

jm = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
)

mycursor = jm.cursor()

sql = "INSERT INTO costumer (name,address) VALUES (%s,%s)"
val = ("Genoveva","Tasi3")

mycursor.execute(sql,val)

jm.commit()

if( mycursor.rowcount > 0 ):
	print("Success inserted!")
else:
	print("Fail inserted!")