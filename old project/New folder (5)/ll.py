import mysql.connector
import threading, socket, struct
import time, datetime
import sys, csv
import hashlib

mydb = mysql.connector.connect(
  host = "null",
  user = "null",
  password = "0000000000",
  database = "python" # you must be sure about data base
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





#python client.py
#Choosing Nickname
#email = input("enter your email?: ")
#passwoed = input("enter your email?: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("51.000.00.58", 3232))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(myemail.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(myemail, input(''))
        client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
rows = len(myreslut)

if rows == 1:
    print("password is correct")
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

    
elif rows == 0:
    print("the password or email is wrong")
