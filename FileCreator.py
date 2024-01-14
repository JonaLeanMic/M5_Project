import time
import csv
import os


# class to write the measured data into a csv file, so it can be downloaded
class FileCreator(object):
    def __init__(self):
        None

    # method to write the data into a csv file
    def writeOutData(self,dataToWrite):
        filename = "M5-" + str(time.ctime().replace(" ", "-").replace(":","-")) +".csv"
        path = os.getcwd() + "/files/" + filename
        print("Filename for new file: ", filename)
        toWrite = []
        header = ['Schwingung', 'Dauer']
        for num in range(0, 10):
            toWrite.append([num+1, ' ', dataToWrite[num]])
        with open(path, 'w', newline="") as file:
            csvwriter = csv.writer(file, quotechar=',')
            csvwriter.writerow(header)
            csvwriter.writerows(toWrite)
        print(toWrite)
        return path  # path in which the data was saved gets returned, so it can be used to download the data from there


