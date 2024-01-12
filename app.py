from flask import Flask, render_template, request
import flask
from measurementManager import MeasurementManager
import RPi.GPIO as GPIO
from flask_socketio import SocketIO


GPIO.setmode(GPIO.BCM)
Interrupt_Pin = 18
GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = Flask(__name__)
socketio = SocketIO(app)

mm = MeasurementManager(Magnet_Pin, socketio)


@app.route('/')
def index():
    return render_template('index.html', data=mm.data, measuring=GPIO.event_detected(Interrupt_Pin))

@app.route('/start_measurement', methods=['POST'])
def start_measurement():
    if request.method == 'POST':
        GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=mm.interrupt, bouncetime=250)
    return render_template('index.html', data=mm.data, measuring=GPIO.event_detected(Interrupt_Pin))

if __name__ == '__main__':
    app.run(debug=True)
