import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(str(data))
    conn.sendall(data)
conn.close()