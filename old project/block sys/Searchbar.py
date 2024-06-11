import mysql.connector

mydb = mysql.connector.connect(
  host = "000000",
  user = "00000",
  password = "0000",
  database = "00000" # you must be sure about data base
)
#python Searchbar.py
#bar = 121212,131313,141414




mycursor = mydb.cursor()

mybar = str(raw_input("Enter your email to show to your info: "))


sql = "SELECT Barcode FROM `Products` WHERE `Barcode` = '"+mybar+"'"

mycursor.execute("SELECT * FROM `Products` WHERE `Barcode` = '"+mybar+"'")

reslut = mycursor.fetchall()


rows = len(reslut)

if rows == 1:
  print("we found", reslut)
elif rows == 0:
    print("not found!!!!!")