import RPi.GPIO as GPIO
from time import sleep

buzzPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23

quarter = .5
eighth = .25
sixteenth = .125

d = 146.83*2

def intro():
        # D
        buzz.start(50)
        buzz.ChangeFrequency(d)
        sleep(quarter)
        # E
        buzz.start(50)
        buzz.ChangeFrequency(d*(9/8))
        sleep(quarter)
        # F
        buzz.start(50)
        buzz.ChangeFrequency(d*(6/5))
        sleep(eighth)
        # C
        buzz.start(50)
        buzz.ChangeFrequency(d*(9/5))
        sleep(quarter)
        # A
        buzz.start(50)
        buzz.ChangeFrequency(d*(3/2))
        sleep(quarter+quarter)
        # Bb
        buzz.start(50)
        buzz.ChangeFrequency(d*(8/5))
        sleep(eighth)
        # A
        buzz.start(50)
        buzz.ChangeFrequency(d*(3/2))
        sleep(quarter+eighth)
        # G
        buzz.start(50)
        buzz.ChangeFrequency(d*(4/3))
        sleep(eighth)


def rif():
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(sixteenth)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(d*(6/5))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(d*(6/5))
    sleep(eighth)
    # E
    buzz.start(50)
    buzz.ChangeFrequency(d*(9/8))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # E 
    buzz.start(50)
    buzz.ChangeFrequency(d*(9/8))
    sleep(sixteenth)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(sixteenth/2)
    buzz.stop()
    sleep(sixteenth/2)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(d*(2/3))
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(d*(2/3))
    sleep(sixteenth/2)
    buzz.stop()
    sleep(sixteenth/2)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(d*(2/3))
    sleep(eighth)
     # F
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/5))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/5))
    sleep(sixteenth)
    # E
    buzz.start(50)
    buzz.ChangeFrequency(d*(5/9))
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # E
    buzz.start(50)
    buzz.ChangeFrequency(d*(5/9))
    sleep(sixteenth)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/5))
    sleep(eighth)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d/2)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d/2)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)

    GPIO.cleanup()

def chorus():
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(sixteenth*.9)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)

def bridge():
    buzz.stop()
    sleep(quarter)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # Rest
    buzz.stop()
    sleep(quarter)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # Rest
    buzz.stop()
    sleep(eighth)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)




try:
    while True:
       intro()
       rif()
       chorus()
       chorus()
       bridge()

        



except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')