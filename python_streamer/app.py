#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/video_feed')
def video_feed():
    camera = Camera()
    return Response(camera.gen_frame(),
                    mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    #ssl_context=('cert.pem', 'key.pem'),
    app.run(host='0.0.0.0',  threaded=True)