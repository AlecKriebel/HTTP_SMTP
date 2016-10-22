# Your EECS account information is:
# Login:	akriebel
# Password:	normal pword

#import socket module
from socket import *
import threading

def handler(connectionSocket, addr):
	try:
		message = connectionSocket.recv(1024).decode()
		filename = None
		if len(message.split()) > 1:
			filename = message.split()[1]
		else:
			filename = '/index.html'
		f = open(filename[1:], "rb") #TODO? Will fail if no file specified (should get index.html)

		outputdata = f.read()

		connectionSocket.send('HTTP/1.1 200 OK\n'.encode('utf-8'))
		connectionSocket.send('Content-Type: text/html\n'.encode('utf-8'))
		connectionSocket.send('\n'.encode('utf-8'))

		#Send the content of the requested file to the client
		for i in range(0,len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])
		connectionSocket.send(b'\r\n\r\n')
		connectionSocket.close()

	except IOError:
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode('utf-8'))
		connectionSocket.close()

def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	# Prepare a server socket
	serverSocket.bind(('', 6789))
	serverSocket.listen(1)
	while True:
		print ("Ready to serve...")
		connectionSocket, addr = serverSocket.accept()
		thread = threading.Thread(target=handler, args=(connectionSocket, addr))
		thread.start()

	serverSocket.close()

if __name__ == '__main__':
	main()
