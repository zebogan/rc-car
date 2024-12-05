import cv2, pygame, numpy, requests, threading

# stream = cv2.VideoCapture('http://10.240.33.129:10001/stream.mjpg')

screen_width, screen_height = 1200, 800
screen=pygame.display.set_mode((screen_width,screen_height))

going = True
direction = None

def send_req(direction):
    try:
        requests.post("http://10.240.33.129:10001", json={'direction': direction})
    except:
        pass

while (going):
    #ret, img = stream.read()
    if True:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = numpy.rot90(img)
        screen.fill(0)
        direction = ''
        #frame=pygame.surfarray.make_surface(img)
        #screen.blit(frame, (0,0))
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    going = False
                    threading.Thread(target=send_req, args=('close',)).start()
                    print('closing')
                elif event.key == pygame.K_w:
                    direction = 'f'
                elif event.key == pygame.K_s:
                    direction = 'b'
                elif event.key == pygame.K_d:
                    direction = 'r'
                elif event.key == pygame.K_a:
                    direction = 'l'
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a]:
                    direction = None
                    threading.Thread(target=send_req, args=('stop',)).start()
        if direction:
            threading.Thread(target=send_req, args=(direction,)).start()

        pygame.time.delay(100)

