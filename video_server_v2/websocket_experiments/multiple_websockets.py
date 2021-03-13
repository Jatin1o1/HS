#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {"value": 0}

USERS = set()
global frame

def camera():
    global frame
    camera=True
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
            return frame
    except:
        pass

def state_event():
    return json.dumps({"type": "state", **STATE})

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    #await notify_users()

async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send("hi")
        
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
