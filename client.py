import cv2, pygame, numpy, requests, threading

server_ip = "10.0.0.22"

screen_width, screen_height = 1200, 800
screen=pygame.display.set_mode((screen_width,screen_height))

going = True
current_directions = set()

stream = cv2.VideoCapture(f'http://{server_ip}:10001/stream.mjpg')

def send_req(direction):
    try:
        requests.post(f"http://{server_ip}:10001", json={'direction': direction})
    except:
        pass

while (stream.isOpened() and going):
    ret, img = stream.read()
    if ret:
        img = numpy.rot90(img)
        img = numpy.flip(img)
        screen.fill(0)
        direction = ''
        frame=pygame.surfarray.make_surface(img)
        screen.blit(frame, (0,0))
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    going = False
                    threading.Thread(target=send_req, args=('close',)).start()
                    print('closing')
                elif event.key == pygame.K_w:
                    current_directions.add('f')
                elif event.key == pygame.K_s:
                    current_directions.add('b')
                elif event.key == pygame.K_d:
                    current_directions.add('r')
                elif event.key == pygame.K_a:
                    current_directions.add('l')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    current_directions.discard('f')
                elif event.key == pygame.K_s:
                    current_directions.discard('b')
                elif event.key == pygame.K_d:
                    current_directions.discard('r')
                elif event.key == pygame.K_a:
                    current_directions.discard('l')
                    threading.Thread(target=send_req, args=('stop',)).start()
        if current_directions:
            combined_direction = ''.join(sorted(current_directions))
            threading.Thread(target=send_req, args=(combined_direction,)).start()
        else:
            threading.Thread(target=send_req, args=('stop',)).start()
            
        pygame.time.delay(100)
