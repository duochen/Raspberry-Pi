from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)
while True:
    conn,address = s.accept()
    print("Received connection from: " + str(address))
    data = "Hello " + address[0] + "\n"
    conn.send(data.encode())    # send data to the client
    conn.close()