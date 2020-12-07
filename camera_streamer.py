import subprocess as sp
import cv2
import imagezmq
import argparse
import time
from imutils.video import VideoStream

rtmpUrl = "rtmp://localhost/live/key"

ap = argparse.ArgumentParser()
ap.add_argument("-D", "--debug-mode", nargs="?"
, const=1, type=bool, default=False, help="if debug on computer or not")
ap.add_argument("-f", "--fps", nargs="?", type=int
, const=1, default=30, help="default is 30 fps")
ap.add_argument("-w", "--witdth", nargs="?", type=int
, const=1, default=1280, help="defualt width is 1280 pixel")
ap.add_argument("-ht", "--height", nargs="?", type=int
, const=1, default=720, help="defualt height is 720 pixel")
args = vars(ap.parse_args())

# if args["debug_mode"] == True:

# In my mac webcamera is 0, also you can set a video file name instead, for example "/home/user/demo.mp4"
path = 0
cap = cv2.VideoCapture(path)

time.sleep(2)
# gather video info to ffmpeg
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# need a method read camera on Pi

# ffmpeg command
command = ['ffmpeg',
    '-y',
    '-f', 'rawvideo',
    '-vcodec','rawvideo',
    '-pix_fmt', 'bgr24',
    '-max_delay', str(100),
    '-s', "{}x{}".format(width, height),
    '-r', str(fps),
    '-i', '-',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'ultrafast',
    '-tune', 'zerolatency',
    '-f', 'flv',
    '-g', '6',
    '-b:v', '400k',
    rtmpUrl]

# pip configuration
p = sp.Popen(command, stdin=sp.PIPE)
        
# read webcamera
while True:
    ret, frame = cap.read()
    if not ret:
        print("frame read failed")
        break
   
    p.stdin.write(frame.tobytes())

