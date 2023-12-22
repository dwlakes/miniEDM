# TODO: "Harmony on the same buzzer doesn't seem possible. 
# Want to try crazy frog bridge into shakira rif or sorry baby. 
# Having trouble with jarring transitions"
'''Fix corrupt object: find .git/objects/ -size 0 -exec rm -f {} \;
# git fetch origin'''


import RPi.GPIO as GPIO
from time import sleep
import threading
import crazyFrogMelody
import crazyFrogBass
import bzrpFmin
import bzrpBass
import shakiraXcrazyFrog
import lights

buzzPin1 = 17
buzzPin2 = 26
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzPin, GPIO.OUT)
#GPIO.setup(buzzPin2, GPIO.OUT)
# buzz1 = GPIO.PWM(buzzPin1, 349.23)
# buzz2 = GPIO.PWM(buzzPin2, 87.32)

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9
       

def playMelody():
    

    ### Idea:
    # bzrpFmin.introPt1()
    # crazyFrogMelody.measure1()
    # bzrpFmin.introPt2()
    # crazyFrogMelody.measure2()
    #crazyFrogMelody.measure3()

    # bzrp_thread = threading.Thread(target=bzrpFmin.intro)
    # #bzrp_thread.start()
    
    #bzrpFmin.sorryBaby()
    #crazyFrogMelody.playIntro()
    crazyFrogMelody.bridge()
    # bzrpFmin.rif()
    # bass_line = threading.Thread(target=playBassLine)
    # bass_line.start()
    # crazyFrogMelody.playIntro()
    #bzrpFmin.sorryBaby()
    #GPIO.cleanup()
    # lights_thread = threading.Thread(target=lightsThread)
    # lights_thread.start()
    #crazyFrogMelody.measure1()
    #     #lights_thread.start()
    # bzrpFmin.rif()
    # bzrp_bass_line = threading.Thread(target=playBzrpBassline)
    # bzrp_bass_line.start()
    # lights_thread = threading.Thread(target=lights.pattern3)
    # lights_thread.start()
    # bzrpFmin.chorus()
    # bzrpFmin.bridge()
    # crazyFrogMelody.playIntro()
    # crazyFrogMelody.playIntro()

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
        print('\nadios')
        exit()
        

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')