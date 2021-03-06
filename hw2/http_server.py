'''Submitted by:
	Alec Kriebel (akriebel, #46541467)
	Zachary Stuart (stuartz. #31362386)
'''
from socket import *
import errno

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 6789))
serverSocket.listen(5)

while True:
	# Establish the connection
	print ("Ready to serve...")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		filename = None
		if len(message.split()) > 1:
			filename = message.split()[1]
		else:
			filename = '/index.html'
		f = open(filename[1:], "rb")

		outputdata = f.read()

		connectionSocket.send('HTTP/1.1 200 OK\n'.encode('utf-8'))

		#Send the content of the requested file to the client
		for i in range(0,len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])
		connectionSocket.send(b'\r\n\r\n')


		connectionSocket.close()
	except IOError as e:
		if e.errno == errno.EPIPE:
			pass
		else:
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode('utf-8'))
			connectionSocket.close()
serverSocket.close()
