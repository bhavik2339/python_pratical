# 53. File Client
import socket

filename = input("Enter file name available on server: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5003))
client.send(filename.encode())

with open("received_" + filename, "wb") as file:
    while True:
        data = client.recv(4096)
        if not data:
            break
        if b"__FILE_END__" in data:
            file.write(data.replace(b"__FILE_END__", b""))
            break
        if b"__FILE_NOT_FOUND__" in data:
            print("File not found on server.")
            break
        file.write(data)

print("File received.")
client.close()
