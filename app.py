from flask import Flask, render_template, request, redirect
from MOCKUPmeasurementManager import MeasurementManager
import json


from flask_classful import FlaskView, route
import random

app = Flask(__name__)


class TestView(FlaskView):
    @route('/')
    def index(self):
        return render_template('index.html')


    @route('/start_measurement')
    def start_measurement(self):

        mm = MeasurementManager.instance()
        #GPIO.output(Magnet_Pin, GPIO.LOW) #magnet ausschalten
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



TestView.register(app, route_base='/')

app.run(debug=True, host='0.0.0.0', port=5000)



while 1:
    None