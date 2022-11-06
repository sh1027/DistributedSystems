# Socket connenction demo
## Contents
### `tcp_echo_server.py`, `tcp_echo_client.py`:
TCP通信のデモプログラム
### `udp_echo_server.py`, `udp_echo_client.py`:
TCP通信のデモプログラム

## Usage & Examples
### TCP 通信
serverを実行させた状態で，clientを実行
#### Server
```sh
python tcp_echo_server.py
# Waiting client connected...
# Client connected. data: b'TCP Hello', addr: ('127.0.0.1', 50555)
```
#### Client 
```sh
python tcp_echo_client.py
# b'Received: TCP Hello'
```

### UDP 通信
serverを実行させた状態で，clientを実行
（※同じPCで実行したため，ServerからClientへの再送信はできていない）
#### Server
```sh
python udp_echo_server.py
# Waiting client connected...
# Client connected. data: b'UDP Hello', addr: ('127.0.0.1', 61770)
```
#### Client 
```sh
python udp_echo_client.py
# 
```