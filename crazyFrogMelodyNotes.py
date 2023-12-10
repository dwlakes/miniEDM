tonicPin = 4
cLED = 6
octaveLED = 21
AbLED = 22
gLED = 27
BbLED = 5
DbLED = 13
EbLED = 19

f = 349.23
f_low = 87.32

quarter = .5*.9
eighth = .25*.9
sixteenth = .125*.9

class Note():
    def __init__(self, freq, duration, rest, LED):
        self.freq = freq
        self.duration = duration
        self.rest = rest 
        self.LED = LED

notesMeasure1 = [Note(f,quarter/2,quarter/2, tonicPin),
                Note(f*(6/5),eighth+(sixteenth/2),sixteenth/2,AbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f,sixteenth/2,sixteenth/2, tonicPin),
                Note(f*(4/3), eighth*.5, eighth/2, BbLED),
                Note(f,eighth/2,eighth/2, tonicPin),
                Note(f*(8/9),eighth/2,eighth/2, EbLED)]

notesMeasure2 = [Note(f,quarter/2,quarter/2, tonicPin),
                 Note(f*(3/2),eighth+(sixteenth/2),sixteenth/2, cLED),
                 Note(f, eighth/2,eighth/2, tonicPin),
                 Note(f,sixteenth/2,sixteenth/2, tonicPin),
                 Note(f*(8/5),eighth*.5,eighth*.5, DbLED),
                 Note(f*(3/2),eighth*.5,eighth*.5, cLED),
                 Note(f*(6/5), eighth*.5,eighth*.5, AbLED)]