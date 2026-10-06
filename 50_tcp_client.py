# 50. TCP/IP Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

client.send("Hello from TCP Client".encode())
reply = client.recv(1024).decode()

print("Server:", reply)
client.close()
