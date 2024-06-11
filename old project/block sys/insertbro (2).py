import mysql.connector
import hashlib

mydb = mysql.connector.connect(
  host = "nulll",
  user = "null",
  password = "00",
  database = "00000" # you must be sure about data base
)

#python insertbro.py
#rightclick then open ter
#faisal@gmail.com
#123123123

mycursor = mydb.cursor()

Barcode =  int(raw_input("enter your Barcode "))
ProductName = str(raw_input("enter ProductName "))
Qty = int(raw_input("enter your Qty "))
WholeSale_Price = int(raw_input("enter your WholeSale_Price "))
Price = int(raw_input("enter price "))



#password_encrypt = hashlib.md5(password.encode()).hexdigest()

sql = "INSERT INTO Products (Barcode, ProductName, Qty, WholeSale_Price, Price) VALUES (%s, %s, %s, %s, %s)"
val = [
  (Barcode, ProductName, Qty, WholeSale_Price, Price),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " was inserted.") 