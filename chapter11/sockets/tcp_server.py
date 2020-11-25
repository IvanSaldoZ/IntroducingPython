# Server TCP
from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 1000
print('Starting the server at', datetime.now())
print('Waiting for a client to call')
# Создаем сокет
# socket.SOCK_STREAM - используем TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Слушаем этот сокет
server.bind(server_address)
server.listen(5)
client, addr = server.accept()
data = client.recv(max_size)
print('At', datetime.now(), client, 'said' ,data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()