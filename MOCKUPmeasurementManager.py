from time import sleep
from random import randrange
from threading import Thread
from FileCreator import FileCreator


# singleton
# siehe https://python-patterns.guide/gang-of-four/singleton/

class MeasurementManager:

    def _init_(self):
        self.start = False
        self.data = []

        self.lastFilePath = ""

    # gibt die momentanen messdaten daten zur�ck
    def getData(self):
        return self.data

    # setzt start auf wahr
    # reinigt list
    # vielleicht speichern wir die Listen in einer Datei?
    def startMeasurement(self):
        if self.start == False:
            print("[MOCKUP] starting measurement")
            self.start = True
            self.setMagnetState(False)
            self.data = []
            self.fakedatathread = Thread(target=self.generateFakeMeasurements)
            self.fakedatathread.start()
        else:
            print("Measurement is in progress")

    # beendet die messung ohne die Liste zu reinigen
    def endMeasurement(self):
        if self.start == True:
            print("[MOCKUP] ending measurement")
            self.start = False
            self.setMagnetState(True)
            FileCreator.writeOutData(self.data)
            try:
                self.fakedatathread.join()
            except Exception as e:
                print("Error in End Measurment, the thread has probably already been ended ")

    # beendet messung, schaltet magnet an, reinigt liste (um neuen Durchgang zu starten wenn etwas schiefgeht)
    def abortMeasurement(self):
        if self.start == True:
            print("aborting measurement")
            self.start = False
            self.setMagnetState(True)
            self.data = []
            try:
                self.fakedatathread.join()
            except Exception as e:
                print("Error in Abort Measurment, the thread has probably already been ended ")
                print(e)

    # gibt messzustand aus
    def getMeasurementStatus(self):
        return self.start

    # �ndert Magnet Zustand
    def setMagnetState(self, state):
        print("Magnetstatus: ", state)

    def generateFakeMeasurements(self):
        counter = 0
        while counter < 10:
            self.data.append(randrange(0, 100))
            counter = counter + 1
            sleep(0.2)
        self.endMeasurement()