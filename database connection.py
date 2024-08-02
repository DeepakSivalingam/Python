import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password=" ",database="python_db")

if connection:
    print("connected")
else:
    print("connection error")