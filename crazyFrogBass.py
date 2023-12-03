import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody

buzzPin = 17
buzzPin2 = 26
tonicLed = 14
gLED = 18
AbLED = 23
BbLED = 24
cLED = 25
DbLED = 12
EbLED = 16
octaveLED = 20

GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)
GPIO.setup(tonicLed, GPIO.OUT)
GPIO.setup(gLED, GPIO.OUT)
GPIO.setup(AbLED, GPIO.OUT)
GPIO.setup(BbLED, GPIO.OUT)
GPIO.setup(cLED, GPIO.OUT)
GPIO.setup(DbLED, GPIO.OUT)
GPIO.setup(EbLED, GPIO.OUT)
GPIO.setup(octaveLED, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)
buzz2 = GPIO.PWM(buzzPin2, 87.32)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

def playBassNote(freq, duration, rest, *LED):
       buzz2.start(50)
       buzz2.ChangeFrequency(freq)
       GPIO.output(LED, 1)
       sleep(duration)
       buzz2.stop()
       GPIO.output(LED, 0)
       sleep(rest)

def bassMeasure1():
        # F
        playBassNote(f_low, quarter*.5, quarter*.5,tonicLed)

        # F
        playBassNote(f_low*2, eighth+(sixteenth/2),sixteenth/2, octaveLED)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2, EbLED)
        
        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2, EbLED)

def bassMeasure2():
        # F
        playBassNote(f_low, quarter*.5, quarter*.5, tonicLed)

        # F + sixteenth rest
        playBassNote(f_low*2, quarter*.5, quarter*.5+sixteenth, octaveLED)

        # C
        playBassNote(f_low*(3/2),sixteenth/2,sixteenth/2, cLED)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2, EbLED)

        # F
        playBassNote(f_low*2,eighth/2,eighth/2, octaveLED)

def bassMeasure3():
        # Db
        playBassNote(f_low*(5/6), quarter*.5, quarter*.5, DbLED)

        # Db
        playBassNote(f_low*(5/6)*2, eighth+(sixteenth/2),sixteenth/2, DbLED)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2, EbLED)
        
        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED)
        
        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)

        # Eb
        playBassNote(f_low*(9/5),eighth/2,eighth/2, EbLED)

        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)

def bassMeasure4():
        # F
        playBassNote(f_low*2,0,quarter+quarter+sixteenth, octaveLED)

        # Eb
        playBassNote(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED)

        # C
        playBassNote(f_low*(3/2),eighth/2,eighth/2, cLED)

        # Bb
        playBassNote(f_low*(4/3),eighth/2,eighth/2, BbLED)
       
        # Ab
        playBassNote(f_low*(6/5),eighth/2,eighth/2, AbLED)
        

def playBassLine():
        bassMeasure1()
        bassMeasure2()
        bassMeasure3()
        bassMeasure4()
