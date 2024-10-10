import socket, cv2, numpy, time

TCP_IP = '10.240.33.129'
#TCP_IP = '10.0.0.22'
TCP_PORT = 10001
BUFFER_SIZE = 160000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 10002))
server.listen()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))

conn, addr = server.accept()
print("setup done")

while True:
    d = b''
    
    sock.settimeout(0.1)

    while True:
        try:
            print("about to get data")
            data = sock.recv(BUFFER_SIZE)
            print("data recvd")
            d += data
            print(len(d))
            if len(d) == 921600:
                break
        except:
            print("breaking")
            break
    
    conn.sendall("RECIEVED".encode())

    print("data done")

    b = bytearray(d)
    print(len(b))
    arr = numpy.array(b).reshape(480, 640, 3)
    cv2.imshow("name", arr)
    cv2.waitKey(10)

cv2.destroyAllWindows()
sock.close()
conn.close()