# 51. Two-way communication - Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5001))

while True:
    message = input("Client: ")
    client.send(message.encode())
    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)
    if reply.lower() == "exit":
        break

client.close()
