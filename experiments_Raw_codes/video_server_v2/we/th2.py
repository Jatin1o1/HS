#!/usr/bin/env python

# WS server that sends camera streams to a web server using opencv


import asyncio
import threading
import websockets
import cv2

global frame

def thread_cam(websocket, path):
    global frame
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
                man = cv2.imencode('.jpg', frame, encode_param)[1]
                frame=man
                websocket.send(man.tobytes())
        except :
            print("error occured")
            pass


# t=threading.Thread(target=cam)
# t.start()

async def time(websocket, path):
    global frame
    t = threading.Thread(target=thread_cam, args=(websocket, path,))
    t.start()
    #await websocket.send(frame.tobytes())


start_server = websockets.serve(time, "127.0.0.1", 9997)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
