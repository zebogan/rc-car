#!/usr/bin/python3

import socket
import time

from picamera2 import Picamera2

#TCP_IP = '10.0.0.102'
TCP_IP = '10.240.35.22'
#TCP_IP = '10.240.33.129'
TCP_PORT = 10002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

picam2 = Picamera2()

config = picam2.create_preview_configuration()
config['main']['format'] = 'RGB888'
print(config)
picam2.configure(config)

picam2.start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 10001))
    sock.listen()

    print("waiting for connection")
    conn, addr = sock.accept()

    client.connect((TCP_IP, TCP_PORT))

    print("setup done")

    while True:
        frame = picam2.capture_array()  
        print("took pic")
        conn.sendall(frame.tobytes())
        print(len(frame.tobytes()))
        print("img sent")
        client.recv(4096)
        
    picam2.stop()
    conn.close()
    client.close()