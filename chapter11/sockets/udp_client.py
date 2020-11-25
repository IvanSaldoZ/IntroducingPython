# Клиент UDP
import socket
from datetime import  datetime
server_address = ('localhost', 6789)
max_size = 4096
print('Starting the client at', datetime.now())
# Создаем сокет
# socket.SOCK_DGRAM - используем UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Отправляем сообщение серверу
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said' ,data)
client.close()