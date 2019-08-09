# THIS CODE SHOWS ALL THE DATABASES IN THE WORK BENCH
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$Wisdom12345"
)

mycursor = mydb.cursor()

# THIS LINE  OF CODE IS USED FOR SHOWING THE DATABASES IN THE SYSTEM
mycursor.execute("SHOW DATABASES")

# PRINTIN THE LIST OF DATABASES
for x in mycursor:
  print(x)
