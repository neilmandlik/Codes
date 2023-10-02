import random
import pywhatkit as p
import socket

host = '192.168.0.101'
port = 3006

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print(f"Received data: {data.decode()}")
number=data.decode()

port = 3007

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print(f"Received data: {data.decode()}")
otp=data.decode()

p.sendwhatmsg_instantly(number,otp,tab_close=True,close_time=5)
