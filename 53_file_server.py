# 53. File Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5003))
server.listen(1)

print("File server waiting...")
conn, addr = server.accept()

filename = conn.recv(1024).decode()
try:
    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            conn.sendall(data)
    conn.sendall(b"__FILE_END__")
except FileNotFoundError:
    conn.sendall(b"__FILE_NOT_FOUND__")

conn.close()
server.close()
