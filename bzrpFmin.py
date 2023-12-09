import RPi.GPIO as GPIO
from time import sleep

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

def playMelodyNote(freq, duration, rest, *LED):
       #print("pin: ",pin)
       buzz = GPIO.PWM(buzzPin, 349.23)
       buzz.start(50)
       buzz.ChangeFrequency(freq)
       GPIO.output(LED, 1)
       sleep(duration)
       buzz.stop()
       GPIO.output(LED, 0)
       sleep(rest)

def intro():
        # F
        buzz.start(50)
        buzz.ChangeFrequency(d)
        sleep(quarter)
        # E
        buzz.start(50)
        buzz.ChangeFrequency(d*(9/8))
        sleep(quarter)
        # F
        buzz.start(50)
        buzz.ChangeFrequency(d*(6/5))
        sleep(eighth)
        # C
        buzz.start(50)
        buzz.ChangeFrequency(d*(9/5))
        sleep(quarter)
        # A
        buzz.start(50)
        buzz.ChangeFrequency(d*(3/2))
        sleep(quarter+quarter)
        # Bb
        buzz.start(50)
        buzz.ChangeFrequency(d*(8/5))
        sleep(eighth)
        # A
        buzz.start(50)
        buzz.ChangeFrequency(d*(3/2))
        sleep(quarter+eighth)
        # G
        buzz.start(50)
        buzz.ChangeFrequency(d*(4/3))
        sleep(eighth)

def transition():
    pwm = GPIO.PWM(lightsQueue.pop(0), 100)
    print("lights q:", lightsQueue)
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
    # F
    playMelodyNote(f, sixteenth, 0, DbLED)
    
    # Ab
    playMelodyNote(f*(6/5), sixteenth*.9, sixteenth*.1, octaveLED)
    
    # Ab
    playMelodyNote(f*(6/5), eighth, 0, octaveLED)
    
    # G
    playMelodyNote(f*(9/8), eighth*.9, eighth*.1, EbLED)
    
    # G
    playMelodyNote(f*(9/8), sixteenth, 0, EbLED)
    
    # F
    playMelodyNote(f, sixteenth, sixteenth, DbLED)

    # F
    playMelodyNote(f, sixteenth/2, sixteenth/2, DbLED)
    
    # F
    playMelodyNote(f, eighth, 0, DbLED)

    # C
    playMelodyNote(f*(3/4), eighth*.9, eighth*.1, AbLED)
    
    # C
    playMelodyNote(f*(3/4), sixteenth, 0, AbLED)
    
    # Bb
    playMelodyNote(f*(2/3), sixteenth, sixteenth, gLED)
    
    # Bb
    playMelodyNote(f*(2/3), sixteenth/2, sixteenth/2, gLED)
    
    # Bb
    playMelodyNote(f*(2/3), eighth, 0, gLED)
    
    # Ab
    playMelodyNote(f*(3/5), eighth*.9, eighth*.1, tonicPin)
  
    # Ab
    playMelodyNote(f*(3/5), sixteenth, 0, tonicPin)
    
    # G
    playMelodyNote(f*(5/9), sixteenth, sixteenth, EbLED)
    
    # G
    playMelodyNote(f*(5/9), sixteenth, 0, EbLED)
   
    # Ab
    playMelodyNote(f*(3/5), eighth, 0, octaveLED)
    
    # f
    playMelodyNote(f/2, eighth*.9, eighth*.1, DbLED )
   
    # f
    playMelodyNote(f/2, eighth*.9, eighth*.1, DbLED )

def chorus(buzz):
     # D
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # D
    buzz.start(50)
    buzz.ChangeFrequency(f)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(sixteenth*.9)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(sixteenth*.9)
    buzz.stop()
    sleep(sixteenth*.1)
    # A (eight)
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(f*(8/9))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(f*(3/4))
    sleep(eighth)

def bridge():
    buzz.stop()
    sleep(quarter)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # Rest
    buzz.stop()
    sleep(quarter)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # D
    buzz.start(50)
    buzz.ChangeFrequency(d)
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
     # A
    buzz.start(50)
    buzz.ChangeFrequency(d*(3/4))
    sleep(eighth)
    # Bb
    buzz.start(50)
    buzz.ChangeFrequency(d*(4/5))
    sleep(eighth)
    # Rest
    buzz.stop()
    sleep(eighth)
    # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)
     # C
    buzz.start(50)
    buzz.ChangeFrequency(d*(8/9))
    sleep(eighth*.9)
    buzz.stop()
    sleep(eighth*.1)




# try:
#     while True:

#        rif(buzz)
#        chorus()
#        chorus()
#        bridge()

        



# except KeyboardInterrupt:
#     GPIO.cleanup()
#     print('\nadios')