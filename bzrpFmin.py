import RPi.GPIO as GPIO
from time import sleep

buzzPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

def intro():
        # F
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


def rif(buzz):
    # F
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(sixteenth)
    # Ab
    buzz.start(50)
    buzz.ChangeFrequency(f*(6/5))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # Ab
    buzz.start(50)
    buzz.ChangeFrequency(f*(6/5))
    sleep(eighth)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(f*(9/8))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(f*(9/8))
    sleep(sixteenth)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(sixteenth/2)
    buzz.stop()
    sleep(sixteenth/2)
    # F
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(eighth)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(f*(2/3))
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(f*(2/3))
    sleep(sixteenth/2)
    buzz.stop()
    sleep(sixteenth/2)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(f*(2/3))
    sleep(eighth)
    # Ab
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/5))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # Ab
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/5))
    sleep(sixteenth)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(f*(5/9))
    sleep(sixteenth)
    # Rest
    buzz.stop()
    sleep(sixteenth)
    # G
    buzz.start(50)
    buzz.ChangeFrequency(f*(5/9))
    sleep(sixteenth)
    # Ab
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/5))
    sleep(eighth)
    # f
    buzz.start(50)
    buzz.ChangeFrequency(f/2)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # f
    buzz.start(50)
    buzz.ChangeFrequency(f/2)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)

def chorus(buzz):
     # D
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(sixteenth*.9)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
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




# try:
#     while True:

#        rif(buzz)
#        chorus()
#        chorus()
#        bridge()

        



# except KeyboardInterrupt:
#     GPIO.cleanup()
#     print('\nadios')