from flask import Flask, render_template, request, redirect
from measurementManager import MeasurementManager
import RPi.GPIO as GPIO
import json


GPIO.setmode(GPIO.BCM)
Magnet_Pin = 23  # achtung nur beispiel zahl, überprüfen
#PIO.setup(Magnet_Pin, GPIO.OUT, initial=GPIO.HIGH) #magnet zu beginn eingeschaltet, Zeile nicht geprüft

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_measurement', methods=['POST'])
def start_measurement():
    if request.method == 'POST':
        mm = MeasurementManager.instance()
        #GPIO.output(Magnet_Pin, GPIO.LOW) #magnet ausschalten
        mm.startMeasurement()
        #hier könnte man auch eine variable start im mm auf true setzen
    return redirect("/")


#api-route für daten
@app.route('/getData', methods=['POST'])
def getJsonDate():
    if request.method == 'POST':
        mm = MeasurementManager.instance()

    return json.dumps(mm.getData())

#api route für systemzustand
@app.route('/getMeasureState')
def getMeasureState():
    mm = MeasurementManager.instance()
    return mm.getMeasurementStatus()

#api-route um messungen abzubrechen (usability)
@app.route('/abort_Measurement')
def abortMeasurement():
    mm = MeasurementManager.instance()
    mm.abortMeasurement()
    return redirect("/")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
