import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody
import crazyFrogBass
import bzrpFmin
import bzrpBass

buzzPin = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)
#buzz = GPIO.PWM(buzzPin, 349.23)
#buzz2 = GPIO.PWM(buzzPin2, 87.32)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9
       

def playMelody():
       crazyFrogMelody.playIntro()
       bass_line = threading.Thread(target=playBassLine)
       bass_line.start()
       crazyFrogMelody.playIntro()
       #GPIO.cleanup()
       bzrpFmin.rif(buzz = GPIO.PWM(buzzPin, 349.23))
       bzrp_bass_line = threading.Thread(target=playBzrpBassline)
       bzrp_bass_line.start()
       bzrpFmin.chorus(buzz = GPIO.PWM(buzzPin, 349.23))
       print('\nadios')

def playBassLine():
    crazyFrogBass.playBassLine()

def playBzrpBassline():
    bzrpBass.playBassline()
        


try:
    while True:
        melody_thread = threading.Thread(target=playMelody)
        #bass_line = threading.Thread(target=playBassLine)
        melody_thread.start()
        #bzrpFmin.rif()
        #bass_line.start()
        #GPIO.cleanup()
        #print('\nadios')
        exit()
        
        



except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')