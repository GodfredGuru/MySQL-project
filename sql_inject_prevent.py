import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$Wisdom12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

# TO PREVENT SQL INJXN WE USE '%s' infront of the equal sign
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
