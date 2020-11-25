# Server UDP
from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096
print('Starting the server at', datetime.now())
print('Waiting for a client to call')
# Создаем сокет
# socket.SOCK_DGRAM - используем UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Слушаем этот сокет
server.bind(server_address)
data, client = server.recvfrom(max_size)
print('At', datetime.now(), client, 'said' ,data)
server.sendto(b'Are you talking to me?', client)
server.close()