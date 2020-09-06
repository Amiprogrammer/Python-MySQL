import mysql.connector

jm = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
)

mycursor = jm.cursor()

sql = "INSERT INTO costumer (name,address) VALUES (%s,%s)"
val = ("Joaquim","Vilaverde 33")

mycursor.execute(sql,val)

jm.commit()

print(mycursor.rowcount, "record inserted!")