import RPi.GPIO as GPIO
from time import sleep
from noteClass import Note
# import miniEDMDriver
import threading
import lights

buzzPin = 17
tonicPin = 4
cLED = 6
octaveLED = 21
AbLED = 22
gLED = 27
BbLED = 5
DbLED = 13
EbLED = 19

GPIO.setup(gLED, GPIO.OUT)
GPIO.setup(AbLED, GPIO.OUT)
GPIO.setup(BbLED, GPIO.OUT)
GPIO.setup(cLED, GPIO.OUT)
GPIO.setup(DbLED, GPIO.OUT)
GPIO.setup(EbLED, GPIO.OUT)
GPIO.setup(octaveLED, GPIO.OUT)
GPIO.setup(tonicPin, GPIO.OUT)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

notesMeasure1 = [Note(f,quarter/2,quarter/2, tonicPin),
                Note(f*(6/5),eighth+(sixteenth/2),sixteenth/2,AbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f,sixteenth/2,sixteenth/2, tonicPin),
                Note(f*(4/3), eighth*.5, eighth/2, BbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f*(8/9),eighth/2,eighth/2, EbLED),
                Note(f,quarter,0, tonicPin),
                Note(f*(9/8), quarter, 0, gLED),
                Note(f*(6/5), eighth, 0, AbLED),
                Note(f*(9/5), quarter, 0, EbLED),
                Note(f*(3/2), quarter+quarter, 0, cLED)]

notesMeasure2 = [Note(f,quarter/2,quarter/2, tonicPin),
                Note(f*(3/2),eighth+(sixteenth/2),sixteenth/2, cLED),
                Note(f, eighth/2,eighth/2, tonicPin),
                Note(f,sixteenth/2,sixteenth/2, tonicPin),
                Note(f*(8/5),eighth*.5,eighth*.5, DbLED),
                Note(f*(3/2),eighth*.5,eighth*.5, cLED),
                Note(f*(6/5), eighth*.5,eighth*.5, AbLED),
                Note(f,quarter,0, tonicPin),
                Note(f*(9/8), quarter, 0, gLED),
                Note(f*(6/5), eighth, 0, AbLED),
                Note(f*2, quarter, 0, octaveLED),
                Note(f*(9/5), quarter+quarter, 0, EbLED)]


def playMelodyNote(freq, duration, rest, *LED):
    #print("pin: ",pin)
    buzz = GPIO.PWM(buzzPin, 349.23)
    buzz.start(50)
    buzz.ChangeFrequency(freq)
    for pin in LED:
        if pin is not None:
            GPIO.output(LED, 1)
    sleep(duration)
    buzz.stop()
    for pin in LED:
        if pin is not None:
            GPIO.output(LED, 0)
    sleep(rest)

def measure1():
    for note in notesMeasure1:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def measure2():
    for note in notesMeasure2:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)