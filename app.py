from flask import Flask, render_template, request, redirect,send_file
from MOCKUPmeasurementManager import MeasurementManager
import json
import glob
import os

#mit diesem code wird der Console-Spam von flask ausgeschaltet 
#beim debuggen von flask-komponenten bitte auskommentieren 
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

from flask_classful import FlaskView, route
import random

app = Flask(__name__)
###

class TestView(FlaskView):
    @route('/')
    def index(self):
        return render_template('index.html')


    @route('/start_measurement')
    def start_measurement(self):

        mm = MeasurementManager.instance()
        #GPIO.output(Magnet_Pin, GPIO.LOW) #magnet ausschalten#
        mm.startMeasurement()
        #hier könnte man auch eine variable start im mm auf true setzen
        return redirect("/")


    #api-route für daten
    @route('/getData')
    def getJsonData(self):

        mm = MeasurementManager.instance()

        return json.dumps(mm.getData())

    #api route für systemzustand
    @route('/getMeasureState')
    def getMeasureState(self):
        mm = MeasurementManager.instance()
        return str(mm.getMeasurementStatus())

    #api-route um messungen abzubrechen (usability)
    @route('/abort_measurement')
    def abortMeasurement(self):
        mm = MeasurementManager.instance()
        mm.abortMeasurement()
        return redirect("/")

    #api-route um messungen abzubrechen (usability)
    @route('/data_download')
    def download(self):
        #nach https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder
        list_of_files = glob.glob(os.getcwd() + "/files/*.csv" ) 
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)

        return send_file(latest_file)

TestView.register(app, route_base='/')

app.run(debug=True, host='0.0.0.0', port=5000)



while 1:
    None