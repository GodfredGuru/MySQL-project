import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 # user name is the root of the computer nothing else.
 user="root",
 # the code below is the password of my mysql
 passwd="$Wisdom12345",
 # SELECTING A DATABASE TO CONNECT TO
 database = 'mydatabase'
)

mycursor = mydb.cursor()

# THIS CODE IS USED FOR CREATING A TABLE NAMED [customers]
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# THIS LINE OF CODE SHOWS THE TABLE [customers] IN MYDATABASE
# NOTE: limit is used to limit the No. of records to view.
mycursor.execute('SELECT *FROM customers LIMIT 6 ')
for x in mycursor:
    print(x)
