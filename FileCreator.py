import time
import csv
import os


#helferklasse schreibt daten in datei zum download 
#nach https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
class FileCreator(object):
    #funktion zum schreiben in datei
    # def writeOutData(self, dataToWrite):
    #     filename = "M5-" + str(time.ctime().replace(" ", "-").replace(":","-")) +".csv"
    #     path = os.getcwd() + "/files/" + filename
    #     print("Filename for new file: ", filename)
    #     #numbers = []
    #     toWrite = []
    #     header = ['Schwingung', 'Dauer']
    #     for num in range(0, 10):
    #         #numbers.append(num)
    #         toWrite.append([num+1, ' ', dataToWrite[num]])
    #     with open(path, 'w', newline="") as file:
    #         csvwriter = csv.writer(file)
    #         csvwriter.writerow(header)
    #         csvwriter.writerows(toWrite)
    #         #csvwriter.wirtecolumns()
    #     print(toWrite)
    #
    #
    #     return path  # Hier wird der Pfad zurückgegeben, um ihn später zu verwenden
    def writeOutData(self, dataToWrite):
        filename = "M5-" + str(time.ctime().replace(" ", "-").replace(":", "-")) + ".csv"
        path = os.path.join(os.getcwd(), "files", filename)
        print("Filename for new file:", filename)

        header = ['Schwingung', 'Dauer']
        fieldnames = ['Nummer der Schwingung', 'Messwert']

        with open(path, 'w', newline="") as file:
            csvwriter = csv.DictWriter(file, fieldnames=fieldnames)

            csvwriter.writeheader()  # Schreibe Kopfzeile

            # Schreibe jede Zeile manuell
            for num, value in enumerate(dataToWrite):
                csvwriter.writerow({fieldnames[0]: num + 1, fieldnames[1]: value})

        return path  # Hier wird der Pfad zurückgegeben, um ihn später zu verwenden


