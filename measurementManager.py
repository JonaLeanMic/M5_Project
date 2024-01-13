import time
from RPi import GPIO

###

#singleton 
#siehe https://python-patterns.guide/gang-of-four/singleton/
class MeasurementManager:

    def __init__(self):
        print('Erstelle neue Manager Instanz')
        self.start = False
        self.timeInterrupt = 0
        self.timePeriodSwing = 0
        self.timeSwingStart = 0
        self.maxSwings = 10
        self.interruptCount = 0
        self.swingCount = 0
        self.start = False
        self.data = []
        GPIO.setmode(GPIO.BCM)
        self.magnet_pin = 23
        self.Interrupt_Pin = 18
        GPIO.setup(self.magnet_pin, GPIO.OUT)
        GPIO.setup(self.Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.Interrupt_Pin, GPIO.FALLING, callback=self.interrupt, bouncetime=250)





    #gibt daten zur�ck
    def getData(self):
        return self.data

    #setzt start auf wahr
    #reinigt list 
    #vielleicht speichern wir die Listen in einer Datei?
    def startMeasurement(self):
        print("starting measurement")
        self.start = True
        self.setMagnetState(False)
        self.data = []


    #beendet die messung ohne die Liste zu reinigen 
    def endMeasurement(self):
        print("ending measurement")
        self.start = False
        self.setMagnetState(False)
        self.swingCount = 0
        self.interruptCount = 0

    #beendet messung, schaltet magnet an, reinigt liste (um neuen Durchgang zu starten wenn etwas schiefgeht)
    def abortMeasurement(self):
        print("aborting measurement")
        self.start = False
        self.setMagnetState(True)
        self.data = []
        self.swingCount = 0
        self.interruptCount = 0
        

    #gibt messzustand aus
    def getMeasurementStatus(self):
        return self.start

    #�ndert Magnet Zustand 
    def setMagnetState(self, state):
        if state:
            GPIO.output(self.magnet_pin, GPIO.HIGH)
        else:
            GPIO.output(self.magnet_pin, GPIO.LOW)

    ## function to stop the time of the last full swing
    def interrupt(self, channel):
        #wenn messung l�uft und noch nicht alle werte gesammelt wurden

        if self.swingCount <= self.maxSwings and self.start:
                    # the first full swings starts after the first interrupt
                    if self.interruptCount == 0:
                        print("start")
                        self.timeInterrupt = time.monotonic()
                    # every second interrupt is a full swing
                    elif self.interruptCount % 2 == 0:
                        print(self.swingCount)
                        self.timeSwingStart = self.timeInterrupt
                        self.timeInterrupt = time.monotonic()
                        self.timePeriodSwing = self.timeInterrupt - self.timeSwingStart
                        print(str(self.timePeriodSwing))

                        self.data.append(self.timePeriodSwing)

                    self.interruptCount += 1
                    self.swingCount = self.interruptCount/2
        else:
            self.endMeasurement()
