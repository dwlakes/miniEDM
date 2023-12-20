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

lightsQueue = [tonicPin, tonicPin, gLED, AbLED, BbLED, cLED, DbLED, EbLED, EbLED]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)

#buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

rifNotes = [Note(f, sixteenth, 0, DbLED), 
    Note(f*(6/5), sixteenth*.9, sixteenth*.1, octaveLED),
    Note(f*(6/5), eighth, 0, octaveLED),
    Note(f*(9/8), eighth*.9, eighth*.1, EbLED),
    Note(f*(9/8), sixteenth, 0, EbLED),
    Note(f, sixteenth, sixteenth, DbLED),
    Note(f, sixteenth/2, sixteenth/2, DbLED),
    Note(f, eighth, 0, DbLED),
    Note(f*(3/4), eighth*.9, eighth*.1, AbLED),
    Note(f*(3/4), sixteenth, 0, AbLED),
    Note(f*(2/3), sixteenth, sixteenth, gLED),
    Note(f*(2/3), sixteenth/2, sixteenth/2, gLED),
    Note(f*(2/3), eighth, 0, gLED),
    Note(f*(3/5), eighth*.9, eighth*.1, tonicPin),
    Note(f*(3/5), sixteenth, 0, tonicPin),
    Note(f*(5/9), sixteenth, sixteenth, EbLED),
    Note(f*(5/9), sixteenth, 0, EbLED),
    Note(f*(3/5), eighth, 0, octaveLED),
    Note(f/2, eighth*.9, eighth*.1, DbLED ),
    Note(f/2, eighth*.9, eighth*.1, DbLED )]

chorusNotes = [Note(f, eighth*.9, eighth*.1),
    Note(f, eighth*.9, eighth*.1),
    Note(f*(8/9), eighth*.9, eighth*.1),
    Note(f*(8/9), sixteenth*.9, 0),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(3/4), sixteenth*.9, sixteenth*.1),
    Note(f*(3/4), eighth*.9, eighth*.1),
    Note(f*(8/9), eighth, 0),
    Note(f*(3/4), eighth, 0)]

bridgeNotes = [Note(f*(3/4), eighth*.9, eighth*.1, cLED),
    Note(f*(3/4), eighth*.9, eighth*.1, cLED),
    Note(f*(8/9), eighth, 0, EbLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(8/9), eighth, 0, EbLED),
    Note(f*(4/5), eighth, quarter, DbLED),
    Note(f, eighth*.9, eighth*.1, BbLED),
    Note(f, eighth*.9, eighth*.1, BbLED),
    Note(f, eighth*.9, eighth*.1, BbLED),
    Note(f*(8/9), eighth*.9, eighth*.1, EbLED),
    Note(f*(8/9), eighth*.9, eighth*.1, EbLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(3/4), eighth, 0, cLED),
    Note(f*(4/5), eighth, 0, DbLED),
    Note(f*(4/5), eighth, eighth, DbLED),
    Note(f*(8/9), eighth, 0, EbLED),
    Note(f*(8/9), eighth, 0, EbLED)]

introNotes = [Note(f,quarter,0, tonicPin),
    Note(f*(9/8), quarter, 0, gLED),
    Note(f*(6/5), eighth, 0, AbLED),
    Note(f*(9/5), quarter, 0, EbLED),
    Note(f*(3/2), quarter+quarter, 0, cLED),
    Note(f*(8/5), eighth, 0, BbLED),
    Note(f*(3/2), quarter+eighth,0, cLED),
    Note(f*(4/3), eighth, 0, BbLED)]

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

def intro():
    for note in introNotes:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)
       

def transition():
    pwm = GPIO.PWM(lightsQueue.pop(0), 100)
    pwm.start(50)
    pwm.ChangeFrequency(20)
    
    count = 0
    for i in range(int(f//2.0), int(f//1.0), 2):
        playMelodyNote(i, 0.04*.9, 0)
        count +=1
        if count % 11 == 0:
            #print("lights q:", lightsQueue)
            pwm.stop()
            pwm = GPIO.PWM(lightsQueue.pop(0), 100)
            pwm.ChangeFrequency(20)
            pwm.start(50)


def rif():
    for note in rifNotes:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def chorus():
    for note in chorusNotes:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)
    
    lights_thread = threading.Thread(target=lights.pattern4)
    lights_thread.start()
    
    for note in chorusNotes:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)

def bridge():
    sleep(quarter)
    for note in bridgeNotes:
        playMelodyNote(note.freq, note.duration, note.rest, note.LED)





# try:
#     while True:

#        rif(buzz)
#        chorus()
#        chorus()
#        bridge()

        



# except KeyboardInterrupt:
#     GPIO.cleanup()
#     print('\nadios')