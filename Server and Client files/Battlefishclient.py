from socket import *

def client():
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('localhost', 1250))
	message = input('Please enter a Player Name: ')
	s.sendall(message.encode())
	print(s.recv(1024))
	while True:
		message = input("Please type something: ")
		s.sendall(message.encode())
		data = s.recv(1024)
		print(data.decode())
	# Send and receive data
		if message == 'quit':
			break
			s.close()
	print('Received: ', data.decode())
	

client()