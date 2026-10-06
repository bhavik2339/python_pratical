# 45. Create a Socket
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5000))
print("Socket created and bound to port 5000.")
s.listen(1)
print("Waiting for a connection...")
conn, address = s.accept()
print("Connected by:", address)
conn.close()
s.close()
