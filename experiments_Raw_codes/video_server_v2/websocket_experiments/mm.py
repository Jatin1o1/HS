#!/usr/bin/env python

# WS server that sends camera streams to a web server using opencv

import asyncio
import websockets
import cv2
import threading


class  wc:
    def __init__(self,websocket, path):
        self.websocket=websocket
        self.path=path
        self.frame= None
        t=threading.Thread(target=self.came)
        t.start()
    
    def came(self):
        while True:
            
            camera = True
            if camera == True:
                vid = cv2.VideoCapture(0)
            else:
                vid = cv2.VideoCapture('videos/video1.mp4')
            try:
                while(vid.isOpened()):
                    img, self.frame = vid.read()
                    self.frame = cv2.resize(self.frame, (640, 480))
                    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 65]
                    man = cv2.imencode('.jpg', self.frame, encode_param)[1]
                    #sender(man)
                    self.websocket.send(man.tobytes())
            except :            
                pass
        




async def time(websocket, path):

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
                #sender(man)
                await websocket.send(man.tobytes())   
        except :            
            pass
        
def cl(websocket,path):
    m=[]
    csl=[]
    if websocket not in m:
        m.append(websocket)
        csl.append("cl_" + str(len(m)))
        csl[1]=wc(websocket,path)
        
        
        
        
    
    
                
start_server = websockets.serve(cl, "127.0.0.1", 9997)    
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


    
    
