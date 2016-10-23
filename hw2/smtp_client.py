'''Submitted by:
	Alec Kriebel (akriebel, #46541467)
	Zachary Stuart (stuartz. #31362386)
'''

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('localhost', 25)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <akriebel@uci.edu>\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250': #if the data is not received
	print('250 reply not received from server.')

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO: <akriebel@uci.edu>\r\n'.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '354':
	print('250 reply not received from server.')

# Send message data.
clientSocket.send('This is an email from a Python client.\r\n')

# Message ends with a single period.
clientSocket.send('.\r\n')
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
clientSocket.close()