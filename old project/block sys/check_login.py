import mysql.connector
import hashlib


mydb = mysql.connector.connect(
  host = "00000",
  user = "0000",
  password = "000",
  database = "customers" # you must be sure about data base
)

#python check_login.py
#rightclick then open ter
#faisal@gmail.com , ddd@hotmail.com
#123123123 , 123123123
# Email =  str(raw_input("enter your email "))
# password = (raw_input("enter Password "))
# 1- INSERT 2- SELECT 3- UPDATE 4- DELETE

mycursor = mydb.cursor()

myemail = raw_input(str("Enter your email to show to your info: "))
mypassword = raw_input(str("Enter your password to show to your info: "))
password_encrypt = hashlib.md5(mypassword.encode()).hexdigest()

sql = "SELECT Email, passowrd FROM `accounts` WHERE `Email` = '"+myemail+"' and `password` = '"+password_encrypt+"'"

mycursor.execute("SELECT * FROM `accounts` WHERE `Email` = '"+myemail+"' and `password` = '"+password_encrypt+"'")

myreslut = mycursor.fetchall()
"""



"""
rows = len(myreslut)

if rows == 1:
    print("password is correct")
elif rows == 0:
    print("the password or email is wrong")



"""
myemail = raw_input(str("Enter your email to show to your info: "))
mypassword = raw_input(str("Enter your password to show to your info: "))

password_encrypt = hashlib.md5(mypassword.encode()).hexdigest()

mycursor.execute('SELECT * FROM accounts WHERE Email = %s AND Password  = %s', (myemail, password_encrypt))



results = mycursor.fetchall()

mydb.commit()


for x in results:
    print(x)
"""