# 52. UDP Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello from UDP Client".encode(), ("localhost", 5002))
data, address = client.recvfrom(1024)

print("Server:", data.decode())
client.close()
