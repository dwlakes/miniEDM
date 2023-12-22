import RPi.GPIO as GPIO
from time import sleep


buzzPin1 = 17
buzzPin2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin1, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)

buzz1 = GPIO.PWM(buzzPin1, 349.23)
buzz2 = GPIO.PWM(buzzPin2, 87.32)