'''
1. This TCP server accepts multiple connections
2. Accepts messages from multiple clients
3. Sends the message to all connected clients
'''

import socket
import threading

host = "localhost"
port = 8000
outstanding = 5
size = 1024 #Bytes

clients = []

#Step-1 Create server side TCP socket
socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Step-2 Bind with host and port
socket_handle.bind((host, port))

#Step-3 Listen for the incoming connections
socket_handle.listen(outstanding)
print("Waiting for connection...")

def client_handler(child_socket, clientaddress):

    clients.append(child_socket)

    while True:
        data = child_socket.recv(size)

        if not data:
            break

        datastring = data.decode('utf-8')
        print("Client says:", datastring)

        # Send message to all connected clients
        for client in clients:
            if client != child_socket:
                client.send(data)

    clients.remove(child_socket)
    child_socket.close()


#Step-4 Accept multiple clients
while True:
    child_socket, clientaddress = socket_handle.accept()

    print("Connected:", clientaddress)

    thread = threading.Thread(
        target=client_handler,
        args=(child_socket, clientaddress)
    )

    thread.start()

socket_handle.close()
