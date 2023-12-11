import RPi.GPIO as GPIO
from time import sleep
import noteClass
import threading
from noteClass import Note

buzzPin = 17
tonicPin = 4
cLED = 6
octaveLED = 21
AbLED = 22
gLED = 27
BbLED = 5
DbLED = 13
EbLED = 19

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(tonicPin, GPIO.OUT)
GPIO.setup(cLED, GPIO.OUT)
GPIO.setup(octaveLED, GPIO.OUT)
GPIO.setup(AbLED, GPIO.OUT)
GPIO.setup(gLED, GPIO.OUT)
GPIO.setup(BbLED, GPIO.OUT)
GPIO.setup(DbLED, GPIO.OUT)
GPIO.setup(BbLED, GPIO.OUT)
GPIO.setup(EbLED, GPIO.OUT)

notesMeasure1 = [Note(f,quarter/2,quarter/2, tonicPin),
                Note(f*(6/5),eighth+(sixteenth/2),sixteenth/2,AbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f,sixteenth/2,sixteenth/2, tonicPin),
                Note(f*(4/3), eighth*.5, eighth/2, BbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f*(8/9),eighth/2,eighth/2, EbLED)]

notesMeasure2 = [Note(f,quarter/2,quarter/2, tonicPin),
                Note(f*(3/2),eighth+(sixteenth/2),sixteenth/2, cLED),
                Note(f, eighth/2,eighth/2, tonicPin),
                Note(f,sixteenth/2,sixteenth/2, tonicPin),
                Note(f*(8/5),eighth*.5,eighth*.5, DbLED),
                Note(f*(3/2),eighth*.5,eighth*.5, cLED),
                Note(f*(6/5), eighth*.5,eighth*.5, AbLED)]

notesMeasure3 = [Note(f, eighth/2, eighth/2, tonicPin),
                Note(f*(3/2), eighth/2, eighth/2, cLED),
                Note(f*2, eighth/2, eighth/2,octaveLED),
                Note(f, sixteenth/2, sixteenth/2, tonicPin),
                Note(f*(8/9),eighth/2,eighth/2, EbLED),
                Note(f*(8/9), sixteenth/2, sixteenth/2, EbLED),
                Note(f*(2/3), eighth/2, eighth/2, cLED),
                Note(f*(9/8), eighth/2, eighth/2, gLED),
                Note(f, quarter/2, quarter/2 + 0.9, tonicPin),
                Note(f*2, quarter/2, quarter/2, octaveLED),
                Note(f*2, quarter/2, quarter/2, octaveLED)]

count = 0

def playMelodyNote(freq, duration, rest, *LED):
       buzz = GPIO.PWM(buzzPin, 349.23)
       #print("pin: ",pin)
       buzz.start(50)
       buzz.ChangeFrequency(freq)
       print("led: ", LED)
       GPIO.output(LED, 1)
       sleep(duration)
       buzz.stop()
       GPIO.output(LED, 0)
       sleep(rest)

def measure1():
        global count
        if count < 1 :
                for note in notesMeasure1:
                        if notesMeasure1.index(note) == 0 or notesMeasure1.index(note) == 1:
                                playMelodyNote(note.freq, note.duration, note.rest, note.LED)
                        else:
                                playMelodyNote(note.freq, note.duration, note.rest)
        else:
                for note in notesMeasure1:
                        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def measure2():
        if count < 1 :
                for note in notesMeasure2:
                        if notesMeasure2.index(note) == 0 or notesMeasure2.index(note) == 1:
                                playMelodyNote(note.freq, note.duration, note.rest, note.LED)
                        else:
                                playMelodyNote(note.freq, note.duration, note.rest)
        else:
                for note in notesMeasure2:
                        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def measure3():
        if count < 1 :
                for note in notesMeasure3:
                        if notesMeasure3.index(note) == 0 \
                        or notesMeasure3.index(note) == 1 \
                        or notesMeasure3.index(note) == 2 \
                        or note == notesMeasure3[-1] \
                        or note == notesMeasure3[-2]:
                                playMelodyNote(note.freq, note.duration, note.rest, note.LED)
                        else:
                                playMelodyNote(note.freq, note.duration, note.rest)
                
        else:
                for note in notesMeasure3:
                        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def playIntro():
    measure1()
    measure2()
    measure3()
    global count
    count +=1
    