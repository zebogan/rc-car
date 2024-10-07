import socket, cv2, numpy, time

#TCP_IP = '10.240.32.228'
TCP_IP = '10.0.0.22'
TCP_PORT = 10001
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))

while True:
    d = b''
    while len(d) < 1228800:
        data = sock.recv(BUFFER_SIZE)
        d += data

    b = bytearray(d)
    arr = numpy.array(b).reshape(480, 640, 4)
    cv2.imshow("name", arr)

cv2.destroyAllWindows()
sock.close()