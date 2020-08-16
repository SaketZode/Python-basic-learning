import socket

tcp_socket = socket.socket()
tcp_socket.connect(("localhost", 7070))
print("Connected")
name = input("Enter Name : ")
tcp_socket.send(bytes(name, "utf-8"))
msg = tcp_socket.recv(1024).decode()
print(msg)

while True:
    message = input("Enter message to send : ")
    tcp_socket.send(bytes(message, "utf-8"))
    rec = tcp_socket.recv(1024).decode()
    print(rec)

tcp_socket.close()
