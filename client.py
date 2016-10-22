from socket import *
import sys
args = sys.argv

s = socket(AF_INET, SOCK_STREAM)                 

s.connect((args[1] , int(args[2])))
s.send(("GET " + str(args[3]) + " HTTP/1.1").encode())
print (s.recv(1024))
s.close()

#Seems to not want to work anymore, even though I changed nothing. Maybe a port binding problem? Not really sure. Got it to work once or twice in the beggining, just alot more of the socket reset errors tho.