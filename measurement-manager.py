import time
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
Interrupt_Pin = 18
GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


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
        self.timeInterrupt = 0
        self.timePeriodSwing = 0
        self.timeSwingStart = 0

        self.maxSwings = 10
        self.interruptCount = 0
        self.swingCount = 0


        self.data = []


    # function to stop the time of the last full swing
    def interrupt(self,channel):

        if self.swingCount <= self.maxSwings:


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

                self.data.append(time)

            self.interruptCount += 1
            self.swingCount = self.interruptCount/2


mm = MeasurementManager()
GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=mm.interrupt, bouncetime=250)
