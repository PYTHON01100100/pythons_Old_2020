import mysql.connector
import hashlib

mydb = mysql.connector.connect(
  host = "null",
  user = "nulll",
  password = "0000",
  database = "customers" # you must be sure about data base
)

#python conn.py
#rightclick then open ter
#faisal@gmail.com
#123123123

mycursor = mydb.cursor()

Email =  str(raw_input("enter your email "))
password = (raw_input("enter Password "))
Fullname = (raw_input("enter your Fullname "))
PhoneNumber = (raw_input("enter your phone number "))

password_encrypt = hashlib.md5(password.encode()).hexdigest()

sql = "INSERT INTO accounts (Email, password, Fullname, PhoneNumber) VALUES (%s, %s, %s, %s)"
val = [
  (Email, password_encrypt, Fullname, PhoneNumber),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " was inserted.") 