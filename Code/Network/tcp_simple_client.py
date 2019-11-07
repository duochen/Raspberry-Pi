from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.python.org", 80))       # Connect
s.send(("GET /index.html HTTP/1.1\n\n").encode())  #Send request
data = s.recv(10000)                    # Get response
print(data)                             # Print response
s.close()                               # Close connection