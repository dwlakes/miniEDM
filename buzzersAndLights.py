import RPi.GPIO as GPIO
from time import sleep


buzzPin1 = 17
buzzPin2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin1, GPIO.OUT)
GPIO.setup(buzzPin2, GPIO.OUT)

buzz1 = GPIO.PWM(buzzPin1, 349.23)
buzz2 = GPIO.PWM(buzzPin2, 87.32)

# First row
tonic1LED = 4
c1LED = 6
octave1LED = 21
Ab1LED = 22
g1LED = 27
Bb1LED = 5
Db1LED = 13
Eb1LED = 19

GPIO.setup(tonic1LED, GPIO.OUT)
GPIO.setup(g1LED, GPIO.OUT)
GPIO.setup(Ab1LED, GPIO.OUT)
GPIO.setup(Bb1LED, GPIO.OUT)
GPIO.setup(c1LED, GPIO.OUT)
GPIO.setup(Db1LED, GPIO.OUT)
GPIO.setup(Eb1LED, GPIO.OUT)
GPIO.setup(octave1LED, GPIO.OUT)

# Second Row
tonic2LED = 14
g2LED = 18
Ab2LED = 23
Bb2LED = 24
c2LED = 25
Db2LED = 12
Eb2LED = 16
octave2LED = 20

GPIO.setup(tonic2LED, GPIO.OUT)
GPIO.setup(g2LED, GPIO.OUT)
GPIO.setup(Ab2LED, GPIO.OUT)
GPIO.setup(Bb2LED, GPIO.OUT)
GPIO.setup(c2LED, GPIO.OUT)
GPIO.setup(Db2LED, GPIO.OUT)
GPIO.setup(Eb2LED, GPIO.OUT)
GPIO.setup(octave2LED, GPIO.OUT)

lightsDictionary = {tonic1LED: GPIO.PWM(tonic1LED, 100),
                    g1LED: GPIO.PWM(g1LED, 100),
                    Ab1LED: GPIO.PWM(Ab1LED, 100),
                    Bb1LED: GPIO.PWM(Bb1LED, 100),
                    c1LED: GPIO.PWM(c1LED, 100),
                    Db1LED: GPIO.PWM(Db1LED, 100),
                    Eb1LED: GPIO.PWM(Eb1LED, 100),
                    octave1LED: GPIO.PWM(octave1LED, 100),

                    tonic2LED: GPIO.PWM(tonic2LED, 100),
                    g2LED: GPIO.PWM(g2LED, 100),
                    Ab2LED: GPIO.PWM(Ab2LED, 100),
                    Bb2LED: GPIO.PWM(Bb2LED, 100),
                    c2LED: GPIO.PWM(c2LED, 100),
                    Db2LED: GPIO.PWM(Db2LED, 100),
                    Eb2LED: GPIO.PWM(Eb2LED, 100),
                    octave2LED: GPIO.PWM(octave2LED, 100),
                    }


row1lights = [tonic1LED, g1LED, Ab1LED, Bb1LED, c1LED, Db1LED, Eb1LED, octave1LED]
row2lights = [tonic2LED, g2LED, Ab2LED, Bb2LED, c2LED, Db2LED, Eb2LED, octave2LED]
allLights = row1lights + row2lights