import RPi.GPIO as gpio
import time

pin11 = 29
pin12 = 31
pin21 = 36
pin22 = 37

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin11, gpio.OUT)
    gpio.setup(pin12, gpio.OUT)
    gpio.setup(pin21, gpio.OUT)
    gpio.setup(pin22, gpio.OUT)

def forward():
    gpio.output(pin11, gpio.HIGH)
    gpio.output(pin12, gpio.LOW)
    gpio.output(pin21, gpio.HIGH)
    gpio.output(pin22, gpio.LOW)

def back():
    gpio.output(pin11, gpio.LOW)
    gpio.output(pin12, gpio.HIGH)
    gpio.output(pin21, gpio.LOW)
    gpio.output(pin22, gpio.HIGH)

def left():
    gpio.output(pin11, gpio.LOW)
    gpio.output(pin12, gpio.HIGH)
    gpio.output(pin21, gpio.HIGH)
    gpio.output(pin22, gpio.LOW)

def right():
    gpio.output(pin11, gpio.HIGH)
    gpio.output(pin12, gpio.LOW)
    gpio.output(pin21, gpio.LOW)
    gpio.output(pin22, gpio.HIGH)

def stop():
    gpio.output(pin11, gpio.LOW)
    gpio.output(pin12, gpio.LOW)
    gpio.output(pin21, gpio.LOW)
    gpio.output(pin22, gpio.LOW)
