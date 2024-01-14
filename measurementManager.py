import time
from RPi import GPIO


# MeasurementManager is managing everything around the sensor, the magnet and the calculation of the measurement data
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

    # returns the list of measurement data
    def getData(self):
        return self.data

    # method to start the process of measurement and sets all important values to 0 and turns of the magnet
    def startMeasurement(self):
        print("starting measurement")
        self.start = True
        self.setMagnetState(False)
        self.data = []
        self.swingCount = 0
        self.interruptCount = 0

    # method to end the measurement when the process is finished correctly
    def endMeasurement(self):
        print("ending measurement")
        self.start = False
        self.setMagnetState(True)
        self.swingCount = 0
        self.interruptCount = 0

    # method that stops the process of measuring if something went wrong, resets all numbers and turns on the magnet
    def abortMeasurement(self):
        print("aborting measurement")
        self.start = False
        self.setMagnetState(True)
        self.data = []
        self.swingCOunt = 0
        self.interruptCount = 0

    # method to return the status of the process
    def getMeasurementStatus(self):
        return self.start

    # returns the count of interrupts
    def getSwingCount(self):
        return self.interruptCount

    # method to turn the magnet on & off
    def setMagnetState(self, state):
        if state:
            GPIO.output(self.magnet_pin, GPIO.HIGH)
        else:
            GPIO.output(self.magnet_pin, GPIO.LOW)

    # function to stop the time of the swings and stores them in data list
    def interrupt(self, channel):

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
                self.timePeriodSwing = round(self.timePeriodSwing,3)
                print(str(self.timePeriodSwing))

                self.data.append(self.timePeriodSwing)
            if self.interruptCount == 20:
                self.endMeasurement()

            self.interruptCount += 1
            self.swingCount = self.interruptCount/2



