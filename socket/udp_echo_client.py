import socket

HOST = "127.0.0.1"
PORT = 50007

# UDP通信
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"UDP Hello", (HOST, PORT))
