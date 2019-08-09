import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$Wisdom12345",
  database="mydatabase"
)

# SELECTING A RECORD FROM A TABLE STARTING FROM A POINT TO A LIMITING POINT
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
