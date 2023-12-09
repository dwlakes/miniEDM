import RPi.GPIO as GPIO
from time import sleep

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

row1lights = [tonic1LED, g1LED, Ab1LED, Bb1LED, c1LED, Db1LED, Eb1LED, octave1LED]
row2lights = [tonic2LED, g2LED, Ab2LED, Bb2LED, c2LED, Db2LED, Eb2LED, octave2LED]
allLights = row1lights + row2lights

def changeLight(duration, light):
    pwm = GPIO.PWM(light, 100)
    pwm.start(50)
    pwm.ChangeFrequency(20) 
    sleep(duration)

def change2Lights(duration, light1, light2):
    pwm1 = GPIO.PWM(light1, 100)
    pwm1.start(50)
    pwm1.ChangeFrequency(20) 
    
    pwm2 = GPIO.PWM(light2, 100)
    pwm2.start(50)
    pwm2.ChangeFrequency(20) 
    sleep(duration)


def pattern1():
    for light in row2lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row2lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row2lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row2lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)

def pattern2():
    print("pattern 2")
    for light in row1lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row1lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row1lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)
    for light in row1lights:
        changeLight(.05, light)
    for light in reversed(row2lights):
        changeLight(.05, light)

def pattern3():
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)
    for light in reversed(row1lights):
        light2 = row2lights[7-row1lights.index(light)]
        change2Lights(.05, light, light2)

    


def startLights():
    pattern1()
    pattern2()
    
