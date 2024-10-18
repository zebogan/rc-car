import RPi.GPIO as gpio
from time import sleep

pin11 = 29
pin12 = 31
pin21 = 36
pin22 = 37
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
GPIO.setup(pin11, gpio.OUT)
GPIO.setup(pin12, gpio.OUT)
GPIO.setup(pin21, gpio.OUT)
GPIO.setup(pin22, gpio.OUT)
