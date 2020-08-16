import socket


tcp_socket = socket.socket()
tcp_socket.bind(("localhost", 7070))
tcp_socket.listen()

while True:
    client_socket, address = tcp_socket.accept()
    name = client_socket.recv(1024).decode()
    client_socket.send(bytes("Hello, {}".format(name), "utf-8"))
    while True:
        msg = client_socket.recv(1024).decode()
        print(msg)
        message = input("Enter message to send to client : ")
        client_socket.send(bytes(message, "utf-8"))
    client_socket.close()
tcp_socket.close()
