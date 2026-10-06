# 52. UDP Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 5002))

print("UDP Server waiting...")
data, address = server.recvfrom(1024)
print("Client:", data.decode())

server.sendto("Hello from UDP Server".encode(), address)
server.close()
