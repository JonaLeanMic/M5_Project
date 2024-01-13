import time
import csv
import os


#helferklasse schreibt daten in datei zum download 
#nach https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
class FileCreator(object):
    #funktion zum schreiben in datei
    def writeOutData(dataToWrite):
        filename = "M5-" + str(time.ctime().replace(" ", "-").replace(":","-")) +".csv"
        path = os.getcwd() + "/files/" + filename
        print("Filename for new file: " , filename)
        toWrite = []
        header = ["Schwingung","Dauer"]
        for num in range(0,10):
            toWrite.append([num+1, dataToWrite[num]])
        with open(path, 'x', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header) 
            csvwriter.writerows(toWrite) 





