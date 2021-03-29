#!/usr/bin/env python
# WS server that sends camera streams to a web server using opencv

import asyncio
import threading
import websockets
import cv2
import time
import json
import logging



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
                frame= frame.tobytes()
                #websocket.send(man.tobytes())
        except :
            print("error occured")
            pass

t=threading.Thread(target=thread_cam)
t.start()

print("camera thread started")


logging.basicConfig()

USERS = set()

async def notify_state():
    global frame
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = frame
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    #await notify_users()


async def cam_send():
    while 1:
        await notify_state()
    
j=threading.Thread(target=cam_send)
j.start()

async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)


start_server = websockets.serve(counter,'127.0.0.1', 9997)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("Server launched")
# give some time for server to start, before we try to connect

