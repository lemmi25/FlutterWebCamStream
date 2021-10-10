import time
import cv2

class Camera(object):
    def __init__(self):
        source = "/dev/video0"
        self.cam = cv2.VideoCapture(source) 
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        #self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def gen_frame(self):  
        while True:
            success, frame = self.cam.read()  # read the camera frame
            if not success:
                continue
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.05)