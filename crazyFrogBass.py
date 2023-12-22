import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody
from noteClass import Note
import buzzers

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
#buzz2 = GPIO.PWM(buzzPin2, 87.32)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

notesMeasure1 = [Note(f_low, quarter*.5, quarter*.5,tonicLed),
        Note(f_low*2, eighth+(sixteenth/2),sixteenth/2, octaveLED),
        Note(f_low*(9/5),eighth/2,eighth/2, EbLED),
        Note(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED),
        Note(f_low*(9/5),eighth/2,eighth/2, EbLED)]

notesMeasure2 = [Note(f_low, quarter*.5, quarter*.5, tonicLed),
        Note(f_low*2, quarter*.5, quarter*.5+sixteenth, octaveLED),
        Note(f_low*(3/2),sixteenth/2,sixteenth/2, cLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED),
        Note(f_low*(9/5),eighth/2,eighth/2, EbLED),
        Note(f_low*2,eighth/2,eighth/2, octaveLED)       
]

notesMeasure3 = [Note(f_low*(5/6), quarter*.5, quarter*.5, DbLED),
        Note(f_low*(5/6)*2, eighth+(sixteenth/2),sixteenth/2, DbLED),
        Note(f_low*(9/5),eighth/2,eighth/2, EbLED),
        Note(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED),
        Note(f_low*(9/5),eighth/2,eighth/2, EbLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED)
]

notesMeasure4 = [Note(f_low*2,0,quarter+quarter+sixteenth, octaveLED),
        Note(f_low*(9/5),sixteenth/2,sixteenth/2, EbLED),
        Note(f_low*(3/2),eighth/2,eighth/2, cLED),
        Note(f_low*(4/3),eighth/2,eighth/2, BbLED),
        Note(f_low*(6/5),eighth/2,eighth/2, AbLED)        
]

def playBassNote(freq, duration, rest, *LED):
        buzz2 = buzzers.buzz2
        buzz2.start(50)
        buzz2.ChangeFrequency(freq)
        GPIO.output(LED, 1)
        sleep(duration)
        buzz2.stop()
        GPIO.output(LED, 0)
        sleep(rest)

def bassMeasure1():
       for note in notesMeasure1:
               playBassNote(note.freq, note.duration, note.rest, note.LED)

def bassMeasure2():
        for note in notesMeasure2:
               playBassNote(note.freq, note.duration, note.rest, note.LED)

def bassMeasure3():
       for note in notesMeasure3:
               playBassNote(note.freq, note.duration, note.rest, note.LED)

def bassMeasure4():
       for note in notesMeasure4:
               playBassNote(note.freq, note.duration, note.rest, note.LED)
        

def playBassLine():
        bassMeasure1()
        bassMeasure2()
        bassMeasure3()
        bassMeasure4()
