import socket
import threading
import sys

nickname = input("Choose your nickname: ")
try:
	# Connecting To Server
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	client.connect(('000', 4444))
	def receive():
		while True:
			try:
				# Receive Message From Server
				# If 'NICK' Send Nickname
				message = client.recv(1024).decode('ascii')
				if message == 'NICK':
					client.send(nickname.encode('ascii'))
				else:
					print(message)
			except:
				# Close Connection When Error
				print("An error occured!")
				client.close()
				break
	
	def write():
		while True:
			try:
				message = '{}: {}'.format(nickname, input(''))
				client.send(message.encode('ascii'))
			except:
				break
    		
	receive_thread = threading.Thread(target=receive)
	receive_thread.start()
	
	write_thread = threading.Thread(target=write)
	write_thread.start()

except:
	print("connection close !")