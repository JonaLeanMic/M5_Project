from flask import Flask, render_template, request, redirect,send_file
from flask_classful import FlaskView, route
from FileCreator import FileCreator
import webbrowser
from threading import Thread
#from MOCKUPmeasurementManager import MeasurementManager
from measurementManager import MeasurementManager
from time import sleep
import json
import pyautogui
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

# class for a flask interface
class TestView(FlaskView):
    @route('/')
    def index(self):
        return render_template('index.html')

    # route to start measurement
    @route('/start_measurement', methods=['POST'])
    def start_measurement(self):

        mm.startMeasurement()
        return redirect("/")

    # api-route for data
    @route('/getData')
    def getJsonData(self):

        return json.dumps(mm.getData())

    # api route to get the status of the process
    @route('/getMeasureState')
    def getMeasureState(self):

        return str(mm.getMeasurementStatus())

    @route('/getSwingCount')
    def getCount(self):
        return str(mm.getSwingCount())

    # api route to stop the program
    @route('/abort_measurement')
    def abortMeasurement(self):

        mm.abortMeasurement()
        return redirect("/")

    # api-route to download the measured data
    @route('/data_download')
    def download(self):
        if not mm.data:
            return "No data available for download."

        file_creator = FileCreator()
        file_path = file_creator.writeOutData(mm.data)
        print("File path:", file_path)

        return send_file(file_path, as_attachment=True,)


# method to start the browser when you open the program
def startBrowser():
    sleep(3)
    webbrowser.open("http://127.0.0.1:5000")
    handled = False
    if not handled:
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('f11')
        handled = True


webThread = Thread(target=startBrowser)
webThread.start()

TestView.register(app, route_base='/')

app.run(debug=True, host='0.0.0.0', port=5000)


while 1:
    print("loop")
