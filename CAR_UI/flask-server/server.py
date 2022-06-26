from flask import Flask, Response
from flask_cors import CORS, cross_origin
import cv2
from AR_RPI import *
from datatest import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def gen_frames():
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def gen_frames1():
    camera1 = cv2.VideoCapture(1)
    while True:
        success, frame = camera1.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route("/members")
@cross_origin()
def members():
    return 'on'


@app.route("/camera")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/camera1")
def video_feed1():
    return Response(gen_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/StartCar")
def EngineOn():
    try:
        if RunningFlag == 0:
            return str(StartCar())
        elif RunningFlag == 1:
            return "Engine is running!!!"

    except:
        return ("No Connection to Relay Controller")


@app.route("/StopCar")
def EngineOff():
    try:
        return str(StopCar())
    except:
        return ("No Connection to Relay Controller")


@app.route("/lockCar")
def lockCar():
    try:
        return str(LockCar())
    except:
        return ("No Connection to Relay Controller")


@app.route("/unlockCar")
def unlockCar():
    try:
        return str(UnlockCar())
    except:
        return ("No Connection to Relay Controller")


@app.route("/lights")
@cross_origin()
def lights():
    try:
        return str(pkl())
    except:
        return ("No Connection to Relay Controller")


@app.route("/Ultrasound")
@cross_origin()
def Ultrasound():
    try:
        return str(randi())
    except:
        return ("No Connection to Sensor")


if __name__ == "__main__":
    app.run(debug=True)
