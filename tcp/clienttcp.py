from socket import*
serverName='DESKTOP-OC56HS8'
serverPort=12532
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("Enter file name")
clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('From server:',filecontents)
clientSocket.close()
