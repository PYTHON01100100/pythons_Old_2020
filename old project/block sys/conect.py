import mysql.connector

mydb = mysql.connector.connect(
  host = "00000",
  user = "0000",
  password = "0000",
  database = "00000"
)

#python conect.py
#rightclick then open ter

mycursor = mydb.cursor()

print("conect")
mycursor.execute("show databases")