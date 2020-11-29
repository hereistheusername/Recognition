# Recognition
Use YOLO model detecting objects in video steam

## Raspberry pi camera check

put `client.py` on Raspberry pi to send video stream to `server.py` on computer

### Step 1 install dependencies

execute this command both on Raspberry pi and computer

> pip install -r requirements.txt

### Step 2 start server

> python server.py

### Step 3 start client

> python client.py -s \<server ip\>

Also can add `-D True` to start client on computer to debug
