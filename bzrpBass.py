import RPi.GPIO as GPIO
from time import sleep

buzzPin = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

def playBassNote(freq, duration, rest):
       buzz2 = GPIO.PWM(buzzPin2, 87.32)
       buzz2.start(50)
       buzz2.ChangeFrequency(freq)
       sleep(duration)
       buzz2.stop()
       sleep(rest)

def measure1():
        # F
        playBassNote(f_low,eighth, 0)

        # F
        playBassNote(f_low*2, eighth, 0)

        # F
        playBassNote(f_low, eighth, 0)

        # F
        playBassNote(f_low*2, eighth, 0)
        
        # F
        playBassNote(f_low, eighth, 0)

        # F
        playBassNote(f_low*2, eighth, 0)

        # F
        playBassNote(f_low, eighth, 0)

        # F
        playBassNote(f_low*2, eighth, 0)

def measure2():
    # F
    playBassNote(f_low, eighth, 0)

    # F
    playBassNote(f_low*2, eighth, 0)

     # F
    playBassNote(f_low, eighth, 0)

    # F
    playBassNote(f_low*2, eighth, 0)

    # Ab
    playBassNote(f_low*(6/5), eighth, 0)

    # Ab
    playBassNote(f_low*(6/5)*2, eighth, 0)

    # Ab
    playBassNote(f_low*(6/5), eighth, 0)

    # Ab
    playBassNote(f_low*(6/5)*2, eighth, 0)

def playBassline():
    measure1()
    measure2()

      