# 50. TCP/IP Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

print("TCP Server waiting for client...")
conn, addr = server.accept()
print("Connected:", addr)

data = conn.recv(1024).decode()
print("Client:", data)

conn.send("Hello from TCP Server".encode())
conn.close()
server.close()
