import threading
import socket
import struct, time
import time
import datetime 

#python server.py
# Connection Data
#host = '518'
#port = 22
#address = (host, port)
host = "518"
port = 4422

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)


# Lists For Clients and Their Nicknames
clients = []
nicknames = []


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)


            """
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast('[Client] {} : {}'.format(nickname, message))
            print('[Client] {} : {}'.format(nickname, message))
            """
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left the chat!'.format(nickname).encode('ascii'))
            print('{} has left the server'.format(nickname).encode('ascii'))
            end_time = time.ctime()
            print("{} has left at {}".format(nickname, end_time))
            #print("you have styed for ", start_time - end_time)
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with IP Address {}".format(str(address)))
        start_time = time.ctime()
        print("you cnnected at {}".format(start_time))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("New user has connected with [ {} ] nickname".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()



print("The Server Established...")
receive()








# link:"https://youtu.be/3UOyky9sEQY"



#python server.py
""" 
i have proplem in calculate how many time you stayed in chat start time - end time
"""