import RPi.GPIO as GPIO
from time import sleep
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

buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

count = 0

def playMelodyNote(freq, duration, rest, *LED):
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
        # F
        playMelodyNote(f,quarter/2,quarter/2, tonicPin)
       
        # Ab
        playMelodyNote(*[f*(6/5),eighth+(sixteenth/2),sixteenth/2] if count < 1 else [f*(6/5),eighth+(sixteenth/2),sixteenth/2,AbLED])
        
        # F
        playMelodyNote(*[f,eighth/2,eighth/2] if count < 1 else [f,eighth/2,eighth/2, tonicPin])
        
        # F
        playMelodyNote(*[f,sixteenth/2,sixteenth/2] if count < 1 else [f,sixteenth/2,sixteenth/2, tonicPin] )
       
        # Bb
        playMelodyNote(*[f*(4/3), eighth*.5, eighth/2] if count < 1 else [f*(4/3), eighth*.5, eighth/2, BbLED])
       
        # F
        playMelodyNote(*[f,eighth/2,eighth/2] if count < 1 else [f,eighth/2,eighth/2, tonicPin])
        
        # Eb
        playMelodyNote(*[f*(8/9),eighth/2,eighth/2] if count < 1 else [f*(8/9),eighth/2,eighth/2, EbLED])

def measure2():
        # F
        playMelodyNote(f,quarter/2,quarter/2, tonicPin)

        # C
        playMelodyNote(f*(3/2),eighth+(sixteenth/2),sixteenth/2, cLED)
       
        # F
        playMelodyNote(*[f,eighth/2,eighth/2] if count < 1 else [f, eighth/2,eighth/2, tonicPin])

        # F
        playMelodyNote(*[f,sixteenth/2,sixteenth/2] if count < 1 else [f,sixteenth/2,sixteenth/2, tonicPin])
       
        # Db
        playMelodyNote(*[f*(8/5),eighth*.5,eighth*.5] if count < 1 else [f*(8/5),eighth*.5,eighth*.5, DbLED])
        
        # C
        playMelodyNote(*[f*(3/2),eighth*.5,eighth*.5] if count < 1 else [f*(3/2),eighth*.5,eighth*.5, cLED])
        
        # Ab
        playMelodyNote(*[f*(6/5), eighth*.5,eighth*.5] if count < 1 else [f*(6/5), eighth*.5,eighth*.5, AbLED])

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
        playMelodyNote(f*2, quarter/2, quarter/2, tonicPin, octaveLED)
        

def playIntro():
    measure1()
    measure2()
    measure3()
    global count
    count +=1
    