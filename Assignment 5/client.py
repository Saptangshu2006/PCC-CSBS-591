import socket
hostname = "localhost"
port = 8000
socket_handle = socket.create_connection((hostname, port))
data = socket_handle.recv(1024)
if data:
    daytime = data.decode("utf-8")
    print("Current Date and Time:", daytime)
socket_handle.close()
