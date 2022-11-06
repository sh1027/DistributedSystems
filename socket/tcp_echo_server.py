import socket

HOST = "127.0.0.1"
PORT = 50007
SOMAXCONN = 1  # 最大接続数

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(SOMAXCONN)
    print("Waiting client connected...")
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Client connected. data: {}, addr: {}".format(data, addr))
                conn.sendall(b"Received: " + data)
