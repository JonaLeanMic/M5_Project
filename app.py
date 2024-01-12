from flask import Flask, render_template, request
from measurementManager import MeasurementManager
import RPi.GPIO as GPIO
from flask_socketio import SocketIO


GPIO.setmode(GPIO.BCM)
Magnet_Pin = 23  # achtung nur beispiel zahl, überprüfen
#PIO.setup(Magnet_Pin, GPIO.OUT, initial=GPIO.HIGH) #magnet zu beginn eingeschaltet, Zeile nicht geprüft

app = Flask(__name__)
socketio = SocketIO(app)

mm = MeasurementManager(Magnet_Pin, socketio)



@app.route('/')
def index():
    return render_template('index.html', data=mm.data)


@app.route('/start_measurement', methods=['POST'])
def start_measurement():
    if request.method == 'POST':
        #GPIO.output(Magnet_Pin, GPIO.LOW) #magnet ausschalten
        mm.start = True
        #hier könnte man auch eine variable start im mm auf true setzen
    return render_template('index.html', data=mm.data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
