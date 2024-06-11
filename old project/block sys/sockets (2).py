import socket

#import sys

host = "0000"
port = 22


"""
ip = socket.gethostbyname('www.google.com')

print(ip)

"""


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
print("welcome")

"""

#python sockets.py
"""