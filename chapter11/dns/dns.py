# DNS (Domain Name System)
import socket
print(socket.gethostbyname('www.yandex.ru'))
print(socket.gethostbyname_ex('www.yandex.ru'))
print(socket.getaddrinfo('www.yandex.ru', 80))
print(socket.getservbyname('http'))
print(socket.getservbyport(80))