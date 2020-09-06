import mysql.connector

jm = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="jmkodigu"
)

mycursor = jm.cursor()

sql = "INSERT INTO costumer (name,address) VALUES (%s,%s)"
val = [
	("Ronaldo","Bidau"),
	("Ebby","Manleu"),
	("Peu amateur","Caicoli"),
	("Aleixo","Aitarak"),
	("Mario","Aimutin"),
	("Azito","Becora")
]

mycursor.executemany(sql,val)

jm.commit()

print(mycursor.rowcount, "was inserted!")