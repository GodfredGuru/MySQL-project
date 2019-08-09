import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$Wisdom12345",
  database="mydatabase"
)

mycursor = mydb.cursor()



mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# this [ %way] IS USED IN ID TO SHOW ADDRESS ENDING WITH 'way'
# EG select *from customer where address =
