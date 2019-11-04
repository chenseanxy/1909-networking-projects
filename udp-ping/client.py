from socket import socket, timeout, AF_INET, SOCK_DGRAM
from time import time_ns    #Python 3.7 required for time_ns()

server = {"addr": "localhost", "port": 12000}

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

for seq in range(10):
    msg = f"ping {seq} {time_ns()}".encode("utf-8")
    start_time = time_ns()
    try:
        client_socket.sendto(msg, (server["addr"], server["port"]))
        recv_msg, addr = client_socket.recvfrom(1024)
        rtt = time_ns() - start_time
        print(f"Received msg {seq}: {recv_msg.decode('utf-8')}, RTT in ns: {rtt}")
    except timeout:
        print(f"Timed out on msg {seq}")
