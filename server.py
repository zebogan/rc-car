#!/usr/bin/python3

import socket
import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput

picam2 = Picamera2()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 10001))
    sock.listen()

    conn, addr = sock.accept()
    picam2.start()
    while True:
        frame = picam2.capture_array()
        print(len(frame.tobytes()))
        conn.send(frame.tobytes())
    picam2.stop()
    conn.close()
