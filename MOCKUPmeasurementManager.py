
from time import sleep
from random import randrange
from threading import Thread

#singleton 
#siehe https://python-patterns.guide/gang-of-four/singleton/



class MeasurementManager(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Nicht erlaubt - rufe instance() um einen Manager zu erhalten ')



    @classmethod
    def instance(self):
        if self._instance is None:
            print('Erstelle neue Manager Instanz')
            self._instance = self.__new__(self)
            self.start = False
            self.data = []

        return self._instance

    #gibt daten zur�ck
    def getData(self):
        return self.data

    #setzt start auf wahr
    #reinigt list 
    #vielleicht speichern wir die Listen in einer Datei?
    def startMeasurement(self):
        if self.start == False:
            print("[MOCKUP] starting measurement")
            self.start = True
            self.setMagnetState(False)
            self.data = []
            self.fakedatathread = Thread(target=generateFakeMeasurements)
            self.fakedatathread.start()
        else:
            print("Measurement is in progress")

    #beendet die messung ohne die Liste zu reinigen 
    def endMeasurement(self):
        print("[MOCKUP] ending measurement")
        self.start = False
        self.setMagnetState(False)
        self.fakedatathread.join()

    #beendet messung, schaltet magnet an, reinigt liste (um neuen Durchgang zu starten wenn etwas schiefgeht)
    def abortMeasurement(self):
        print("aborting measurement")
        self.start = False
        self.setMagnetState(True)
        self.data = []
        self.fakedatathread.join()

    #gibt messzustand aus 
    def getMeasurementStatus(self):
        return self.start

    #�ndert Magnet Zustand 
    def setMagnetState(self, state):
        print("Magnetstatus: " , state)

def generateFakeMeasurements():
    mm = MeasurementManager.instance()
    counter = 0
    while counter < 10:
        mm.data.append( randrange(0,100))
        counter = counter + 1 
        sleep(1)
    mm.endMeasurement()