import pymysql

db = pymysql.connect(host="localhost", user="root", passwd=MY_PASSWORD_FOR_ROOT_USER)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS books_db")
cursor.execute("SHOW DATABASES")

cursor.close()
db.close()

for databases in cursor:
    print(databases)
