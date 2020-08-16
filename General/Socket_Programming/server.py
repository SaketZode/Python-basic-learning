import socket

tcp_socket = socket.socket()

tcp_socket.bind(("localhost", 7070))

tcp_socket.listen()
print("TCP server started")

while True:
    client_socket, address = tcp_socket.accept()
    print("Connected with {}".format(address))
    msg = client_socket.recv(1024).decode()
    client_socket.send(bytes("Welcome, {}".format(msg), "utf-8"))
