import cv2
import time
import numpy as np
import core.utils as utils
import tensorflow as tf
from core.yolov3 import YOLOv3, decode
from PIL import Image

input_size   = 416

def get_object(video_url, threshold=0.45):
    input_layer  = tf.keras.layers.Input([input_size, input_size, 3])
    feature_maps = YOLOv3(input_layer)

    bbox_tensors = []
    for i, fm in enumerate(feature_maps):
        bbox_tensor = decode(fm, i)
        bbox_tensors.append(bbox_tensor)

    model = tf.keras.Model(input_layer, bbox_tensors)
    utils.load_weights(model, "yolov3_union_10000.weights")
    model.summary()

    vid = cv2.VideoCapture(video_url)
    while True:
        return_value, frame = vid.read()
        if return_value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            return "No image"
        frame_size = frame.shape[:2]
        image_data = utils.image_preporcess(np.copy(frame), [input_size, input_size])
        image_data = image_data[np.newaxis, ...].astype(np.float32)

        prev_time = time.time()
        pred_bbox = model.predict_on_batch(image_data)
        curr_time = time.time()
        exec_time = curr_time - prev_time

        pred_bbox = [tf.reshape(x, (-1, tf.shape(x)[-1])) for x in pred_bbox]
        pred_bbox = tf.concat(pred_bbox, axis=0)
        bboxes = utils.postprocess_boxes(pred_bbox, frame_size, input_size, 0.3)
        bboxes = utils.nms(bboxes, threshold, method='nms')
        image = utils.draw_bbox(frame, bboxes)

        result = np.asarray(image)
        info = "time: %.2f ms" %(1000*exec_time)
        cv2.putText(result, text=info, org=(50, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=(255, 0, 0), thickness=2)

        result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        retval, buffer = cv2.imencode(".jpeg", image)
        yield ((b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n'))



