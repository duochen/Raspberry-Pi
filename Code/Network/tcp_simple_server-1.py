from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(10)
conn,address = s.accept()
print("Received connection from: " + str(address))
while True:
    data = conn.recv(1024).decode()
    if not data:
        # if data is not received, break
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    conn.send(data.encode())    # send data to the client

c.close()