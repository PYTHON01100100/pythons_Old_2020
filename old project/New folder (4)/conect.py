import mysql.connector

mydb = mysql.connector.connect(
  host = "000",
  user = "000",
  password = "00",
  database = "00"
)

#python conect.py
#rightclick then open ter

mycursor = mydb.cursor()

print("conect")
mycursor.execute("show databases")