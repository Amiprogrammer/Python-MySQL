import mysql.connector

# connection to database server
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mysql_training"
)

mycursor = mydb.cursor()

# function to include the view date
def view_date():
    global mycursor
    mycursor.execute("SELECT name,gender,address FROM estudent")
    result = mycursor.fetchall()
    num_of_table = len(result)
    print(66*"_")
    print("|No \t |Name \t\t\t |Gender \t |Address \t |")
    for i,x in zip(range(1,num_of_table),result):
        print(66*"_")
        print(f"|{i} \t |{x[0]} \t |{x[1]} \t\t |{x[2]} \t |")
    print(66*"_")

# function to include the insert date
def insert_date():
    global mycursor
    print("=== Insert new date ===")
    name = str(input("name: "))
    gender = str(input("gender (m/f): "))
    address = str(input("address: "))

    sql = "INSERT INTO estudent (name,gender,address) VALUES (%s,%s,%s)"
    val = (name,gender,address)
    mycursor.execute(sql,val)

    mydb.commit()

    if( mycursor.rowcount > 0 ):
        print(mycursor.rowcount, "record(s) inserted!")
    else:
        print(mycursor.rowcount, "record(s) not inserted!")

def delete_date(x):
    global mycursor
    x = x.lower()
    sql = "DELETE FROM estudent WHERE name = %s"
    val = (x,)
    mycursor.execute(sql,val)

    mydb.commit()

    if( mycursor.rowcount > 0 ):
        print(mycursor.rowcount, "record(s) deleted!")
    else:
        print(mycursor.rowcount, "record(s) not deleted!")

def update_date():
    pass

print("=== Databases Application ===")

# check user choose her with handling error
while True:
    try:
        print("""\n\
        choose what are you doing?
        1). view date
        2). insert date
        3). edit date
        4). delete date
        """)
        user_choose = str(input("\ntype number here: "))

        if( user_choose == "1" ):
            # call view_date function
            view_date()
        elif( user_choose == "2" ):
            # call insert_date function
            insert_date()
        elif( user_choose == "3" ):
            # call update_date function
            update_date()
        elif( user_choose == "4" ):
            id = str(input("you want to delete.(type name) "))
            delete_date(id)
        elif( user_choose.lower() == "quit" or user_choose.lower() == "exit"):
            break
        else:
            print("not match!")# QUESTION:
            break
    except Exception as err:
        print(":-< can't get \"input\"!")
        print(err)
