import RPi.GPIO as gpio
from time import sleep

pin11 = 29
pin12 = 31
pin21 = 36
pin22 = 37
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(pin11, gpio.OUT)
gpio.setup(pin12, gpio.OUT)
gpio.setup(pin21, gpio.OUT)
gpio.setup(pin22, gpio.OUT)
