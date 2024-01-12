import time
from RPi import GPIO
from flask_socketio import SocketIO, emit

GPIO.setmode(GPIO.BCM)
Interrupt_Pin = 18
GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class MeasurementManager:

    def __init__(self, magnet_pin, socketio):
        self.start = False
        self.timeInterrupt = 0
        self.timePeriodSwing = 0
        self.timeSwingStart = 0

        self.maxSwings = 10
        self.interruptCount = 0
        self.swingCount = 0
        self.start = False
        self.data = []
        self.magnet_pin = magnet_pin
        self.socketio = socketio

        GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=self.interrupt, bouncetime=250)

    #def is_magnet_on(self):
        #return GPIO.input(self.magnet_pin) == GPIO.HIGH

    # function to stop the time of the last full swing
    def interrupt(self, channel):
        #if not self.is_magnet_on():
        if self.start:
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
                    self.socketio.emit('data_update', self.data, namespace='/socket')

                self.interruptCount += 1
                self.swingCount = self.interruptCount/2
