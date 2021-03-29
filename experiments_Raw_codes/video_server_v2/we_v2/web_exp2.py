#!/usr/bin/env python
# WS server that sends camera streams to a web server using opencv

import asyncio
import threading
import websockets
import cv2
import time

global frame

def thread_cam():
    global frame
    print("camera thread strted")
    while True:
        camera = True
        if camera == True:
            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture('videos/video1.mp4')
        try:
            while(vid.isOpened()):
                img, frame = vid.read()
                frame = cv2.resize(frame, (640, 480))
                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 65]
                frame = cv2.imencode('.jpg', frame, encode_param)[1]
                #websocket.send(man.tobytes())
        except :
            print("error occured")
            pass

t=threading.Thread(target=thread_cam)
t.start()

async def hello(websocket, path):
    global frame
    while 1:
        await websocket.send(frame.tobytes())
    #print("sent frame")

def start_loop(loop, server):
    loop.run_until_complete(server)
    loop.run_forever()

# start a new event loop
new_loop = asyncio.new_event_loop()
start_server = websockets.serve(hello, '127.0.0.1', 9994, loop=new_loop)
j = threading.Thread(target=start_loop, args=(new_loop, start_server))
j.start()

print("Server launched")
# give some time for server to start, before we try to connect
time.sleep(2)
