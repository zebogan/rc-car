import cv2, pygame, numpy

stream = cv2.VideoCapture('http://10.240.33.129:8000/stream.mjpg')

screen_width, screen_height = 1200, 800
screen=pygame.display.set_mode((screen_width,screen_height))

while (stream.isOpened()):
    ret, img = stream.read()
    if ret:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = numpy.rot90(img)
        screen.fill(0)
        frame=pygame.surfarray.make_surface(img)
        screen.blit(frame, (0,0))
        pygame.display.flip()