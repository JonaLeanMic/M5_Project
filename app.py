from flask import Flask, render_template, request, redirect,send_file
from flask_classful import FlaskView, route
from FileCreator import FileCreator
import webbrowser
from threading import Thread
from MOCKUPmeasurementManager import MeasurementManager
from time import sleep
import json
import glob
import os

#mit diesem code wird der Console-Spam von flask ausgeschaltet 
#beim debuggen von flask-komponenten bitte auskommentieren 
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



app = Flask(__name__)

mm = MeasurementManager()
print(mm.start)
####

class TestView(FlaskView):
    @route('/')
    def index(self):
        return render_template('index.html')


    @route('/start_measurement', methods = ['POST'])
    def start_measurement(self):
        mm.startMeasurement()
        return redirect("/")


    #api-route für daten
    @route('/getData')
    def getJsonData(self):
        return json.dumps(mm.getData())

    #api route für systemzustand
    @route('/getMeasureState')
    def getMeasureState(self):
        return str(mm.getMeasurementStatus())

    @route('/getSwingCount')
    def getCount(self):
        return str(mm.getSwingCount())

    #api-route um messungen abzubrechen (usability)
    @route('/abort_measurement')
    def abortMeasurement(self):

        mm.abortMeasurement()
        return redirect("/")

    #api-route um messungen abzubrechen (usability)

    @route('/data_download')
    def download(self):
        if not mm.data:
            return "No data available for download."

        file_creator = FileCreator()
        file_path = file_creator.writeOutData(mm.data)
        print("File path:", file_path)

        return send_file(file_path, as_attachment=True,)

def startBrowser():
    sleep(3)
    webbrowser.open("http://127.0.0.1:5000")

    
webThread = Thread(target=startBrowser)
webThread.start()

TestView.register(app, route_base='/')

app.run(debug=True, host='0.0.0.0', port=5000)





while 1:
    print("loop")