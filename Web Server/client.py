from socket import *
import sys


clientSocket=socket(AF_INET, SOCK_STREAM)
serverName=sys.argv[1]
serverPort=int(sys.argv[2])
fileName=sys.argv[3]
message="GET "+"/"+fileName+" HTTP/1.1"

clientSocket.connect((serverName,serverPort))
clientSocket.send(message)
receivedMessage=clientSocket.recv(2048)
print(receivedMessage)
clientSocket.close()



