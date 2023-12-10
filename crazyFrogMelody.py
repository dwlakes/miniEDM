import RPi.GPIO as GPIO
from time import sleep
import crazyFrogMelodyNotes
import threading

buzzPin = 17
tonicPin = 4
cLED = 6
octaveLED = 21
AbLED = 22
gLED = 27
BbLED = 5
DbLED = 13
EbLED = 19

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

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

count = 0

def playMelodyNote(freq, duration, rest, *LED):
       buzz = GPIO.PWM(buzzPin, 349.23)
       #print("pin: ",pin)
       buzz.start(50)
       buzz.ChangeFrequency(freq)
       GPIO.output(LED, 1)
       sleep(duration)
       buzz.stop()
       GPIO.output(LED, 0)
       sleep(rest)

def measure1():
        global count
        if count < 1 :
                for note in crazyFrogMelodyNotes.notesMeasure1:
                        if crazyFrogMelodyNotes.notesMeasure1.index(note) == 0 or crazyFrogMelodyNotes.notesMeasure1.index(note) == 1:
                                playMelodyNote(note.freq, note.duration, note.rest, note.LED)
                        else:
                                playMelodyNote(note.freq, note.duration, note.rest)
        else:
                for note in crazyFrogMelodyNotes.notesMeasure1:
                        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def measure2():
        if count < 1 :
                for note in crazyFrogMelodyNotes.notesMeasure2:
                        if crazyFrogMelodyNotes.notesMeasure2.index(note) == 0 or crazyFrogMelodyNotes.notesMeasure2.index(note) == 1:
                                playMelodyNote(note.freq, note.duration, note.rest, note.LED)
                        else:
                                playMelodyNote(note.freq, note.duration, note.rest)
        else:
                for note in crazyFrogMelodyNotes.notesMeasure2:
                        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def measure3():
        # F
        playMelodyNote(f, eighth/2, eighth/2, tonicPin)
        
        # C
        playMelodyNote(f*(3/2), eighth/2, eighth/2, cLED)
        
        # F
        playMelodyNote(f*2, eighth/2, eighth/2,octaveLED)
       
        # F
        playMelodyNote(*[f, sixteenth/2, sixteenth/2] if count < 1 else [f, sixteenth/2, sixteenth/2, tonicPin])
       
        # Eb
        playMelodyNote(*[f*(8/9),eighth/2,eighth/2] if count < 1 else [f*(8/9),eighth/2,eighth/2, EbLED])
        
        # Eb
        playMelodyNote(*[f*(8/9), sixteenth/2, sixteenth/2] if count < 1 else [f*(8/9), sixteenth/2, sixteenth/2, EbLED])
       
        # Middle C
        playMelodyNote(*[f*(2/3), eighth/2, eighth/2] if count < 1 else [f*(2/3), eighth/2, eighth/2, cLED])
        
        # G
        playMelodyNote(*[f*(9/8), eighth/2, eighth/2] if count < 1 else [f*(9/8), eighth/2, eighth/2, gLED])
        
        # F
        playMelodyNote(*[f, quarter/2, quarter/2] if count < 1 else [f, quarter/2, quarter/2, tonicPin])
     
        sleep(.9)
        # F
        playMelodyNote(f*2, quarter/2, quarter/2, tonicPin, octaveLED)
       
        # F 
        playMelodyNote(*[f*2, quarter/2, quarter/2, tonicPin, octaveLED] if count < 1 else [f*2, quarter/2, 0, tonicPin, octaveLED])
        

def playIntro():
    pass
    measure1()
    measure2()
    measure3()
    global count
    count +=1
    