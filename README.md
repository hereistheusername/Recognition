# Recognition
Use YOLO model detecting objects in video steam

## uv4l installation guide

Assuming camera has been activated on Raspberry pi

```
curl https://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
```

```
deb https://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main
```

```
sudo apt-get update
sudo apt-get install uv4l uv4l-raspicam
```

```
sudo apt-get install uv4l-raspicam-extras
```

```
sudo apt-get install uv4l-server uv4l-uvc uv4l-xscreen uv4l-mjpegstream uv4l-dummy uv4l-raspidisp
```

Then, restart service

```
sudo service uv4l_raspicam restart
```



If meet the problem that libssl1.0 is missing, do the following

```
wget https://packages.debian.org/stretch/armhf/libssl1.0.2/download
sudo apt install ./<replace with file name>
```

If all succeeded, you can see the video at [http://\<your raspberry pi ip>:8080/stream](http://<your raspberry pi ip>:8080/stream)

## Capture Video using OpenCV in Python

```python
vid = cv2.VideoCapture('http://<your raspberry pi ip>:8080/stream/video.mjpeg')
```

