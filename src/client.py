from socket import socket, AF_INET, SOCK_STREAM
from sys import argv



HOST, PORT = "localhost", 1300
data = " ".join(argv[1:])


with socket(AF_INET, SOCK_STREAM) as sock:

    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, "utf-8"))
    sock.sendall(b"\n")

    received = str(sock.recv(1024), "utf-8")

print("Sent:    {}".format(data))
print("Received: ", received)