import RPi.GPIO as GPIO
from time import sleep
import buzzersAndLights

# First row
tonic1LED = 4
c1LED = 6
octave1LED = 21
Ab1LED = 22
g1LED = 27
Bb1LED = 5
Db1LED = 13
Eb1LED = 19

GPIO.setmode(GPIO.BCM)

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

# GPIO.setup(tonic2LED, GPIO.OUT)
# GPIO.setup(g2LED, GPIO.OUT)
# GPIO.setup(Ab2LED, GPIO.OUT)
# GPIO.setup(Bb2LED, GPIO.OUT)
# GPIO.setup(c2LED, GPIO.OUT)
# GPIO.setup(Db2LED, GPIO.OUT)
# GPIO.setup(Eb2LED, GPIO.OUT)
# GPIO.setup(octave2LED, GPIO.OUT)


row1lights = [tonic1LED, g1LED, Ab1LED, Bb1LED, c1LED, Db1LED, Eb1LED, octave1LED]
row2lights = [tonic2LED, g2LED, Ab2LED, Bb2LED, c2LED, Db2LED, Eb2LED, octave2LED]
allLights = row1lights + row2lights

def changeLight(duration, light):
    pwm = buzzersAndLights.lightsDictionary[light]
    pwm.start(50)
    pwm.ChangeFrequency(20) 
    sleep(duration)
    GPIO.output(light, 0)
    pwm.stop()

def change2Lights(duration, light1, light2):
    pwm1 = buzzersAndLights.lightsDictionary[light1]
    pwm1.start(50)
    pwm1.ChangeFrequency(20) 
    
    pwm2 = buzzersAndLights.lightsDictionary[light2]
    pwm2.start(50)
    pwm2.ChangeFrequency(20) 
    sleep(duration)
    GPIO.output(light1, 0)
    GPIO.output(light2, 0)
    pwm1.stop()
    pwm2.stop()

def change4Lights(duration, light1, light2, light3, light4):
    pwm1 = buzzersAndLights.lightsDictionary[light1]
    pwm1.start(50)
    pwm1.ChangeFrequency(20) 
    
    pwm2 = buzzersAndLights.lightsDictionary[light2]
    pwm2.start(50)
    pwm2.ChangeFrequency(20) 

    pwm3 = buzzersAndLights.lightsDictionary[light3]
    pwm3.start(50)
    pwm3.ChangeFrequency(20) 
    
    pwm4 = buzzersAndLights.lightsDictionary[light4]
    pwm4.start(50)
    pwm4.ChangeFrequency(20) 
    sleep(duration)
    GPIO.output(light1, 0)
    GPIO.output(light2, 0)
    GPIO.output(light3, 0)
    GPIO.output(light4, 0)
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()


def pattern1():
    for i in range(4):
        for light in row2lights:
            changeLight(.05, light)
        for light in reversed(row2lights):
            changeLight(.05, light)
    
    
def pattern2():
    print("pattern 2")
    for i in range(5):
        for light in row1lights:
            changeLight(.05, light)
        for light in reversed(row2lights):
            changeLight(.05, light)


def pattern3():
    for i in range(9):
        for light in reversed(row1lights):
            light2 = row2lights[7-row1lights.index(light)]
            change2Lights(.05, light, light2)


def pattern4():
    for i in range(8):
        for light in row1lights[4:8]:
            light2 = row1lights[7-row1lights.index(light)]
            light3 = row2lights[row1lights.index(light)]
            light4 = row2lights[7-row1lights.index(light)]
            change4Lights(.05, light, light2, light3, light4) 
        for light in reversed(row1lights[4:8]):
            light2 = row1lights[7-row1lights.index(light)]
            light3 = row2lights[row1lights.index(light)]
            light4 = row2lights[7-row1lights.index(light)]
            change4Lights(.05, light, light2, light3, light4) 
    
    

def pattern5():
    changeLight(.05, row1lights[3])  
    changeLight(.05, row1lights[5])
    changeLight(.05, row1lights[2])
    changeLight(.05, row1lights[4])
    changeLight(.05, row1lights[1])
    changeLight(.05, row1lights[7])
    changeLight(.05, row1lights[0])

def pattern6():
    change2Lights(.05, row1lights[7], row2lights[4])  
    change2Lights(.05, row1lights[0], row2lights[1])
    change2Lights(.05, row1lights[3], row2lights[7])
    change2Lights(.05, row1lights[2], row2lights[0])
    change2Lights(.05, row1lights[5], row2lights[3])
    change2Lights(.05, row1lights[4], row2lights[2])
    change2Lights(.05, row1lights[1], row2lights[5])

def pattern7():
    for i in range(5):
        for light in row1lights:
            changeLight(.05, light)
            changeLight(.05, row2lights[row1lights.index(light)])
        for light in reversed(row1lights):
            changeLight(.05, light)
            changeLight(.05, row2lights[row1lights.index(light)])


def pattern8ZigZig():

    for i in range(5):
        for light in row1lights:
            if row1lights.index(light) %2 == 0:
                changeLight(.05, light)
            else:
                changeLight(.05, row2lights[row1lights.index(light)])

        for light in reversed(row1lights):
            if row1lights.index(light) %2 == 0:
                changeLight(.05, row2lights[row1lights.index(light)])
            else: 
                changeLight(.05, light)

def pattern9Snake():
    for i in range(6):
        for i in range(0,8,2):
            # start top 
            changeLight(.05, row1lights[i])
            changeLight(.05, row2lights[i])

            #start bottom
            changeLight(.05, row2lights[i+1])
            changeLight(.05, row1lights[i+1])

        for i in reversed(range(0,8,2)):
            # start top 
            changeLight(.05, row1lights[i])
            changeLight(.05, row2lights[i])

            #start bottom
            changeLight(.05, row2lights[i+1])
            changeLight(.05, row1lights[i+1])

def pattern2and3():
    pattern2()
    pattern3()
   

def randomPattern():
    for i in range(4):
        pattern5()
  
    for i in range(5):
        pattern6()


def sevenAnd5():
    pattern7()
    for i in range(4):
        pattern5()
    pattern6()
    pattern4()
   
        


def startLights():
    pattern1()
    pattern2()



