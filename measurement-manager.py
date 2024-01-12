import time
from RPi import GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
Interrupt_Pin = 18
GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# class MeasurementManager(object):
#     _instance = None


class MeasurementManager:

    # timeStart = 0
    # timeInterrupt = time.monotonic()
    # timeLastSwing = 0
    #
    # maxSwings = 0
    # swingCount = -1
    # interruptCount = 0
    #
    # data = []

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(MeasurementManager, cls).__new__(cls)
    #         return cls._instance

    def __init__(self):
        self.timeStart = 0
        self.timeInterrupt = time.monotonic()
        self.timeLastSwing = 0

        self.maxSwings = 0
        self.swingCount = 0
        self.interruptCount = 0

        self.data = []

    def test(self):
        print("test")
        #self.interrupt()
        print("works")

    # function to stop the time of the last full swing
    def interrupt(self):



        # the first full swings starts after the first interrupt
        if self.swingCount == 0:
            self.timeStart = time.monotonic()
            print(self.timeStart)
            print("start")

        # every second interrupt is a full swing##
        if self.swingCount % 2 == 0:

            self.timeLastSwing = time.monotonic()
            print(self.timeLastSwing)
            self.addMeasurement(self.timeLastSwing)

        self.swingCount += 1

    def addMeasurement(self,time):
        self.data.append(time)
        print(self.data)



def testing():
    print("t3est")

mm = MeasurementManager()
GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=testing, bouncetime=250)
