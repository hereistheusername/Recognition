import cv2
import time

def get_frame_from_ftmp(rtmp_addr):

    cap = cv2.VideoCapture(rtmp_addr)
    time.sleep(2)

    while True:

        ret = cap.read()
        yield ret
