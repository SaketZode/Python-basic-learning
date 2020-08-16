import socket

tcp_socket = socket.socket()

tcp_socket.connect(("localhost", 7070))
print("Connected..")
tcp_socket.send(bytes("Saket", "utf-8"))
msg = tcp_socket.recv(1024).decode()
print(msg)
