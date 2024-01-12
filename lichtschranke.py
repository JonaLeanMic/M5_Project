from RPi import GPIO
from measurementManager import MeasurementManager
class Lichtschranke:

    def __init__(self):
        Interrupt_Pin = 18
        GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        mm = MeasurementManager()
        GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=Interrupt, bouncetime=250)


