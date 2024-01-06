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
import lightsPatterns
import LCD1602

LCD1602.init(0x27, 1)

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
    

    crazyFrogMelody.playIntro()
    bass_line = threading.Thread(target=playBassLine)
    bass_line.start()
    crazyFrogMelody.playIntro()
    bass_line.join()
    crazyFrogMelody.bridge()
    crazyFrogMelody.measure1()
    bzrpFmin.introPt1()
    bass_thread = threading.Thread(target=crazyFrogBass.bassMeasure1)
    bass_thread.start()
    
    crazyFrogMelody.measure1()
    bzrpFmin.introPt2()

    bass_thread = threading.Thread(target=crazyFrogBass.bassMeasure2)
    bass_thread.start()
    crazyFrogMelody.measure2()
    bass_thread = threading.Thread(target=crazyFrogBass.bassMeasure3)
    bass_thread.start()
    crazyFrogMelody.measure3()
    bass_thread.join()
    crazyFrogBass.bassMeasure4()
    crazyFrogMelody.bridge()
    crazyFrogMelody.measure1()
    bzrpFmin.introPt2()
    lights_thread = threading.Thread(target=lightsPatterns.pattern1)
    lights_thread.start()
    bzrpFmin.rif()

    bzrp_bass_line = threading.Thread(target=playBzrpBassline)
    bzrp_bass_line.start()
    lights_thread = threading.Thread(target=lightsPatterns.pattern3)
    lights_thread.start()
    bzrpFmin.chorus()
    lights_thread.join()

    # fix
    lights_thread = threading.Thread(target=lightsPatterns.pattern2and3)
    lights_thread.start()
    bzrpFmin.bridgePt1()
    bassBridgeThread = threading.Thread(target=bzrpBass.playBridgeNotes)
    bassBridgeThread.start()

    #make pattern 7 + random and longer
    lights_thread = threading.Thread(target=lightsPatterns.sevenAnd5)
    lights_thread.start()
    bzrpFmin.bridgePt2()
    bzrpFmin.sorryBaby()

    lights_thread = threading.Thread(target=lightsPatterns.pattern8ZigZig)
    lights_thread.start()
    bassSorryBabyThread = threading.Thread(target=bzrpBass.playSorryBabyNotes)
    bassSorryBabyThread.start()
    
    # make pattern 9 longer
    lights_thread = threading.Thread(target=lightsPatterns.pattern9Snake)
    lights_thread.start()
    bzrpFmin.sorryBabyPt2()
    bassSorryBabyThread.join()
    bassThread = threading.Thread(target=bzrpBass.chorus)
    bassThread.start()
    bzrpFmin.introPt1()
    bzrpFmin.playOutroNotes()

    rando_lights = threading.Thread(target=lightsPatterns.randomPattern)
    rando_lights.start()
    crazyFrogMelody.playIntro()
  


    # print('\nadios')
    # LCD1602.write(5,0, 'Ciao')
    # LCD1602.write(6,1, ';)')

def playBassLine():
    crazyFrogBass.playBassLine()

def bassMeasure1():
    crazyFrogBass.bass()

def playBzrpBassline():
    bzrpBass.playBassline()

def lightsThread():
    lightsPatterns.startLights()
        


try:
    while True:
        # LCD1602.clear()
        # break
        melody_thread = threading.Thread(target=playMelody)
        # # bass_line = threading.Thread(target=playBassLine)
        melody_thread.start()

        # rando_lights = threading.Thread(target=lights.pattern6)
        # rando_lights.start()
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