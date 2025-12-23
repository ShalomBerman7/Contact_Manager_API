import mysql.connector


conn = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "0000",
    database= "DB")

cursor = conn.cursor()
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
