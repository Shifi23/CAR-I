from flask import Flask, Response
from flask_cors import CORS, cross_origin
import cv2

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
global status
status = 1






def gen_frames():
    camera = cv2.VideoCapture(4)
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
    camera1 = cv2.VideoCapture(6)
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


@app.route("/lights")
@cross_origin()
def lights():
    global status
    if status == 1:
        status = 0
        return 'on'
    else:
        status = 1
        return 'off'


@app.route("/camera")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/camera1")
def video_feed1():
    return Response(gen_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
