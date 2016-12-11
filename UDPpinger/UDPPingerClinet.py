from socket import *
from datetime import datetime
import sys


clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)
serverName=sys.argv[1]
serverPort=int(sys.argv[2])

for sequence_number in range(1,11):
    previous = datetime.now()
    message="Ping "+str(sequence_number)+" "+str(previous)
    clientSocket.sendto(message,(serverName,serverPort))
    try:
        receivedMessage=clientSocket.recv(2048)
        current= datetime.now()
        elapsedTime=current-previous
        print(receivedMessage+" "+"RTT: "+"0."+str(elapsedTime).split(".")[1]+" seconds")
    except timeout:
        print("Request timed out")
