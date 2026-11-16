import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)
server_socket.bind(("0.0.0.0", 9000))
server_socket.listen()
print(server_socket)

while True:
    client_socket, client_address = server_socket.accept()  # similar to input()
    print(client_socket, client_address)

    client_request = client_socket.recv(1024)  # similar to input()
    print(client_request)
    
    message = b"HTTP/1.1 200 OK\r\n\r\n<h1>Wow</h1>"
    client_socket.send(message)

    client_socket.close()


server_socket.close()
print("FINISHED")