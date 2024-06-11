import mysql.connector

mydb = mysql.connector.connect(
  host = "000",
  user = "0000",
  password = "0000",
  database = "000000"
)

#python lol.py
#rightclick then open ter

mycursor = mydb.cursor()

mybar = raw_input(int("Enter barcode: ")

#sql = " SELECT * FROM customers WHERE Barcode = %s "
#sql = " SELECT Barcode FROM `Products` WHERE `Barcode` = '"+mybar+"' "

#mycursor.execute("SELECT Barcode FROM customers")
#mycursor.execute("SELECT * FROM `Products` WHERE `Barcode` = '"+mybar+"'")

mycursor.fetchall()

mycursor.execute(sql)
print("conect")
