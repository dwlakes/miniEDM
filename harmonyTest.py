import RPi.GPIO as GPIO
from time import sleep
import threading

buzzPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)

buzz = GPIO.PWM(buzzPin, 349.23)


def play_tonic():
    buzz.start(50)
    buzz.ChangeFrequency(349.23)
    sleep(15)
    buzz.stop()
    buzz.ChangeDutyCycle(0)  # Ensuring PWM is off

def play_third():
    buzz.start(50)
    buzz.ChangeFrequency(349.23*(4/3))
    sleep(5)
    buzz.stop()
    buzz.ChangeDutyCycle(0)  # Ensuring PWM is off

try:
    tonicThread = threading.Thread(target=play_tonic)
    thirdThread = threading.Thread(target=play_third)
    
    tonicThread.start()
    sleep(1)
    thirdThread.start()
    
    tonicThread.join()  # Wait for threads to finish
    thirdThread.join()

    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')
