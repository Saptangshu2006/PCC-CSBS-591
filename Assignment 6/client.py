import socket
import threading

hostname = "localhost"
port = 8000
size = 1024

#1. create a socket Connection
socket_handle = socket.create_connection((hostname, port))

#2. Receive messages from server
def receive_message():

    while True:
        data = socket_handle.recv(size)

        if data:
            print("Message from Server:", data.decode('utf-8'))
        else:
            break


# Start receiving messages
thread = threading.Thread(target=receive_message)
thread.daemon = True
thread.start()


#3. Send messages to server
while True:

    message = input("Client says: ")

    if message == "exit":
        break

    socket_handle.send(message.encode('utf-8'))


#4. Then close
socket_handle.close()
