# 51. Two-way communication - Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5001))
server.listen(1)

print("Server waiting...")
conn, addr = server.accept()
print("Connected:", addr)

while True:
    message = conn.recv(1024).decode()
    if not message or message.lower() == "exit":
        break
    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())
    if reply.lower() == "exit":
        break

conn.close()
server.close()
