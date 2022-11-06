import socket

HOST = "127.0.0.1"
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Waiting client connected...")
    while True:
        data, addr = s.recvfrom(1024)
        print("Client connected. data: {}, addr: {}".format(data, addr))
