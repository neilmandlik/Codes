import socket

host = '192.168.0.101'
port = 3006

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

data_to_send = "Hello MNNU!"
client_socket.send(data_to_send.encode())

client_socket.close()