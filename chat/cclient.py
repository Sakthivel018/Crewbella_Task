import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',1000))
name = input("Your name: ")
message=input(">>> ")
message = name+" >>> "+message
client.sendall(message.encode())
while message!="end":
    data=client.recv(1000).decode()
    if data:
        print(data)
        message=input(">>> ")
        client.sendall(message.encode())
    else:
        break
client.close()