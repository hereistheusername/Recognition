import object_detection_api
import os
from PIL import Image
from flask import Flask, render_template, Response
import  cv2

video_url = 'http://192.168.199.119:8080/stream/video.mjpeg'
video_url = 'rtmp://192.168.199.105/live/key'
video_url = './docs/road.mp4'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/test')
# def test():
# 
#     PATH_TO_TEST_IMAGES_DIR = 'object_detection/test_images'  # cwh
#     TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3)]
# 
#     image = Image.open(TEST_IMAGE_PATHS[0])
#     objects = object_detection_api.get_objects(image)
# 
#     return objects

@app.route('/detect')
def detect():
    return Response(object_detection_api.get_object(video_url),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)