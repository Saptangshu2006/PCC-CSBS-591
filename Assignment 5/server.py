import socket
from datetime import datetime
hostname = "localhost"
port = 8000
socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_handle.bind((hostname, port))
socket_handle.listen(5)
print("Daytime Server is waiting for client...")
child_socket, client_address = socket_handle.accept()
print("Client connected:", client_address)
daytime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
child_socket.sendall(daytime.encode("utf-8"))
child_socket.close()
socket_handle.close()
