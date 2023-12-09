import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody
import crazyFrogBass
import bzrpFmin
import bzrpBass
import lights

buzzPin = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
#GPIO.setup(buzzPin2, GPIO.OUT)
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
       lights_thread = threading.Thread(target=lightsThread)
       lights_thread.start()
        # lights_thread.start()
       bzrpFmin.transition()
       bzrpFmin.rif()
       bzrp_bass_line = threading.Thread(target=playBzrpBassline)
       bzrp_bass_line.start()
       lights_thread = threading.Thread(target=lights.pattern3)
       lights_thread.start()
       bzrpFmin.chorus(buzz = GPIO.PWM(buzzPin, 349.23))
       print('\nadios')

def playBassLine():
    crazyFrogBass.playBassLine()

def playBzrpBassline():
    bzrpBass.playBassline()

def lightsThread():
    lights.startLights()
        


try:
    while True:
        melody_thread = threading.Thread(target=playMelody)
        bass_line = threading.Thread(target=playBassLine)
        melody_thread.start()
        # bzrpFmin.transition()
        # lights_thread = threading.Thread(target=lightsThread)
        # lights_thread.start()
        # bzrpFmin.rif()
        #bass_line.start()
        #GPIO.cleanup()
        #print('\nadios')
        exit()
        
        



except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')