#import socket module

from socket import *
from thread import *
from time import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort=6092
serverSocket.bind(('',serverPort))
serverSocket.listen(1)



def response_thread(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024)

        try:
            filename = message.split()[1]
        except IndexError:
            print(message)
            return


        f = open(filename[1:])

        outputdata =[]

        #Send one HTTP header line into socket
        outputdata.append('HTTP/1.1 200 OK\n')
        outputdata.append('Content-Type:text/html\n')
        outputdata.append('\n')
        outputdata.append(f.read())

        #Send the content of the requested file to the client
        correctResponse=""

        for i in range(0, len(outputdata)):

            correctResponse+=outputdata[i]

        connectionSocket.send(correctResponse)
        connectionSocket.close()

    except IOError:
        # Send response message for file not found

        errorResponse="HTTP/1.1 404 Not Found"
        connectionSocket.send(errorResponse)

        #Close client socket
        connectionSocket.close()


while True:
    #Establish the connection

    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()
    start_new_thread(response_thread,(connectionSocket,addr))


serverSocket.close()


