from AI_vision import AI_cam

k=AI_cam(cam_address="rtsp://admin:admin@192.168.1.152:554")
k.start_detection()
print("url cam  started detection")