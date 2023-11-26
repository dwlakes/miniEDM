import RPi.GPIO as GPIO
from time import sleep
import threading

buzzPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

def playMelodyNote(freq, duration, rest):
       buzz.start(50)
       buzz.ChangeFrequency(freq)
       sleep(duration)
       buzz.stop()
       sleep(rest)

def measure1():
        # F
        playMelodyNote(f,quarter/2,quarter/2)
       
        # Ab
        playMelodyNote(f*(6/5),eighth+(sixteenth/2),sixteenth/2)
        
        # F
        playMelodyNote(f,eighth/2,eighth/2)
        
        # F
        playMelodyNote(f,sixteenth/2,sixteenth/2)
       
        # Bb
        playMelodyNote(f*(4/3), eighth*.5, eighth/2)
       
        # F
        playMelodyNote(f,eighth/2,eighth/2)
        
        # Eb
        playMelodyNote(f*(8/9),eighth/2,eighth/2)

def measure2():
        # F
        playMelodyNote(f,quarter/2,quarter/2)

        # C
        playMelodyNote(f*(3/2),eighth+(sixteenth/2),sixteenth/2)
       
        # F
        playMelodyNote(f,eighth/2,eighth/2)

        # F
        playMelodyNote(f,sixteenth/2,sixteenth/2)
       
        # D
        playMelodyNote(f*(8/5),eighth*.5,eighth*.5)
        
        # C
        playMelodyNote(f*(3/2),eighth*.5,eighth*.5)
        
        # Ab
        playMelodyNote(f*(6/5), eighth*.5,eighth*.5)

def measure3():
       # F
        buzz.start(50)
        buzz.ChangeFrequency(f)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        #buzz.start(50)
        # C
        buzz.ChangeFrequency(f*(3/2))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # Eb
        buzz.ChangeFrequency(f*(8/9))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # Eb
        buzz.ChangeFrequency(f*(8/9))
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # Middle C
        buzz.ChangeFrequency(f*(2/3))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # G
        buzz.ChangeFrequency(f*(9/8))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        sleep(1)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)

def playIntro():
    measure1()
    measure2()
    measure3()
    