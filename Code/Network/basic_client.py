import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.84', 50000))
s.sendall('Hello, world'.encode())
data = s.recv(1024)
s.close()
print('Received ', str(data))