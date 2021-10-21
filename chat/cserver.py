import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',1000))
server.listen(1)
connection, client_address = server.accept()
print("Connected with:", client_address)
name = input("Your name: ")
message = ""
while message!="end":
    data = connection.recv(1000).decode()
    if data:
        print( data)
        message = input()
        message = name+">>> "+message
        connection.sendall(message.encode())
    else:
        break
connection.close()
server.close()
    