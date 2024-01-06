import RPi.GPIO as GPIO
from time import sleep
from noteClass import Note
import buzzersAndLights

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

bridgeSusNotes = [Note(f_low, quarter*6, 0, None),
                  Note(f_low*(6/5), quarter+quarter, 0, None),
                  Note(f_low*(4/3), quarter*6, 0, None),
                  Note(f_low*(9/8), quarter, 0, None),
                  Note(f_low*(4/3), eighth/2, eighth/2, None),
                  Note(f_low*(4/3), eighth/2, eighth/2, None),
                  Note(f_low, quarter*6, 0, None),
                  Note(f_low*(6/5), quarter+quarter, 0, None),
                  Note(f_low*(4/3), quarter*6, 0, None)]

sorryBabyPt2Notes = [Note(f_low, eighth, 0, None),
                     Note(f_low*2, eighth, quarter, None),
                     Note(f_low, eighth, 0, None),
                     Note(f_low*2, eighth, quarter, None),
                     
                     Note(f_low, eighth, 0, None),
                     Note(f_low*2, eighth, quarter, None),
                     Note(f_low*(6/5), eighth, 0, None),
                     Note((f_low*(6/5))*2, eighth, quarter, None),
                     
                     Note(f_low*(4/5), eighth, 0, None),
                     Note(f_low*(8/5), eighth, quarter, None),
                     Note(f_low*(4/5), eighth, 0, None),
                     Note(f_low*(8/5), eighth, quarter, None),
                     
                     Note(f_low*(2/3), eighth, 0, None),
                     Note(f_low*(4/3), eighth, quarter, None),
                     Note(f_low*(2/3), eighth, 0, None),
                     Note(f_low*(4/3), eighth, quarter, None),

                     Note(f_low*(4/5), eighth, 0, None),
                     Note(f_low*(8/5), eighth, quarter, None),
                     Note(f_low*(4/5), eighth, 0, None),
                     Note(f_low*(8/5), eighth, quarter, None)]


def playBridgeNotes():
        for note in bridgeSusNotes:
                playBassNote(note.freq, note.duration, note.rest, note.LED)

def playBassNote(freq, duration, rest, *LED):
       buzz2 = buzzersAndLights.buzz2
       buzz2.start(50)
       buzz2.ChangeFrequency(freq)
       sleep(duration)
       buzz2.stop()
       sleep(rest)

def playSorryBabyNotes():
      for note in sorryBabyPt2Notes:
            playBassNote(note.freq, note.duration, note.rest, note.LED)

def chorus():
    for note in bassChorusNotes:
        playBassNote(note.freq, note.duration, note.rest, note.LED)


def playBassline():
    chorus()

      