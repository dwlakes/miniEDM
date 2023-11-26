import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody

buzzPin = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)
buzz2 = GPIO.PWM(buzzPin2, 87.32)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

def playBassNote(freq, duration, rest):
       buzz2.start(50)
       buzz2.ChangeFrequency(freq)
       sleep(duration)
       buzz2.stop()
       sleep(rest)


def bassMeasure1():
        # F
        playBassNote(f_low, quarter*.5, quarter*.5)

        # F
        playBassNote(f_low*2, eighth+(sixteenth/2),sixteenth/2)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2)
        
        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2)

def bassMeasure2():
        # F
        playBassNote(f_low, quarter*.5, quarter*.5)

        # F + sixteenth rest
        playBassNote(f_low*2, quarter*.5, quarter*.5+sixteenth)

        # C
        playBassNote(f_low*(3/2),sixteenth/2,sixteenth/2)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2)

        # F
        playBassNote(f_low*2,eighth/2,eighth/2)

def bassMeasure3():
        # Db
        playBassNote(f_low*(5/6), quarter*.5, quarter*.5)

        # Db
        playBassNote(f_low*(5/6)*2, eighth+(sixteenth/2),sixteenth/2)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2)
        
        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2)

        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)

def bassMeasure4():
        # F
        playBassNote(f_low*2,0,quarter+quarter+sixteenth)

        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2)

        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2)

        # Bb
        playBassNote(f_low*(4/3),eighth/2,eighth/2)
       
        # Ab
        playBassNote(f_low*(6/5),eighth/2,eighth/2)
        

def playBassLine():
        bassMeasure1()
        bassMeasure2()
        bassMeasure3()
        bassMeasure4()
