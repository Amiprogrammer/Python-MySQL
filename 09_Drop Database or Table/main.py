import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testing2")
# mycursor.execute("CREATE TABLE costumer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("DROP TABLE IF EXISTS costumer")

mycursor.execute("DROP DATABASE IF EXISTS testing2")
