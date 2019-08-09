import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$Wisdom12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

# commit is needed to make changes or make the changes be effected.
mydb.commit()

print(mycursor.rowcount, "record(s) affected")
