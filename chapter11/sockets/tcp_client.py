# Клиент TCP
import socket
from datetime import  datetime
server_address = ('localhost', 6789)
max_size = 1000
print('Starting the client at', datetime.now())
# Создаем сокет
# socket.SOCK_STREAM - используем TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Соединяемся
client.connect(server_address)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied' ,data)
client.close()