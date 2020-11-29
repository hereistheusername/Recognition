from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
from flask import Flask, render_template, Response
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
 help="ip address of the server to which the client will connect")
ap.add_argument("-D", "--debug-mode", nargs="?", const=1,
type=bool, default=False, help="if debug on personal computer or not")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
	args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
if args["debug_mode"] == True:
    vs = VideoStream(src=0).start()
else:
    vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
 

# stream server

while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	sender.send_image(rpiName, frame)