import RPi.GPIO as GPIO
from time import sleep
from noteClass import Note

buzzPin = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

bassChorusNotes = [Note(f_low,eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low, eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low, eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low, eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low, eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low, eighth, 0),
    Note(f_low*2, eighth, 0),
    Note(f_low*(6/5), eighth, 0),
    Note(f_low*(6/5)*2, eighth, 0),
    Note(f_low*(6/5), eighth, 0),
    Note(f_low*(6/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(8/5), eighth, 0),
    Note(f_low*(8/5)*2, eighth, 0),
    Note(f_low*(4/3), eighth, 0),
    Note(f_low*(4/3)*2, eighth, 0),
    Note(f_low*(4/3), eighth, 0),
    Note(f_low*(4/3)*2, eighth, 0)
    
]

def playBassNote(freq, duration, rest, *LED):
       buzz2 = GPIO.PWM(buzzPin2, 87.32)
       buzz2.start(50)
       buzz2.ChangeFrequency(freq)
       sleep(duration)
       buzz2.stop()
       sleep(rest)

def chorus():
    for note in bassChorusNotes[0:int(len(bassChorusNotes)/2)]:
        playBassNote(note.freq, note.duration, note.rest, note.LED)


def playBassline():
    chorus()

      