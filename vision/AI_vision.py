
import os
import random
from glob import glob
from statistics import mode
from tqdm import tqdm
import cv2
import pandas as pd
import joblib
import threading
import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.mixture import GaussianMixture
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
base = "jump/"
rtb = None
device_IDs = 10
training_img_size=64


class AI_cam:
    active_cams_obj=0  # total AI camera objects
    active_cams_detection=0 # total AI camera Using realtime_detection
    
    def __init__(self,cam_address=""):
        AI_cam.active_cams_obj +=1     # increase camera count to one
        self.camera_add=cam_address

    def start_detection(self):
        self.t=threading.Thread(target=self.prediction_by_master)  
        AI_cam.active_cams_detection +=1  # increase count of camera Using AI
        self.t.start()       
    
    def stop_detection(self):
        self.t.stop()
        AI_cam.active_cams_detection -= 1  # decrease count of camera Using AI

    def prediction_by_master(self):
        # clf1 = MLPClassifier(hidden_layer_sizes=(1024,), batch_size=256, verbose=True, early_stopping=True)
        # clf2 = SVC()
        # clf3 = RandomForestClassifier()
        # clf4 = GradientBoostingClassifier()
        # clf5 = KNeighborsClassifier()
        # clf6 = GaussianNB()
        # clf7 = GaussianMixture()

        clf1 = joblib.load(base + "models/MLPClassifier.sav")
        clf2 = joblib.load(base + "models/SVClassfier.sav")
        clf3 = joblib.load(base + "models/RandomForestClassifier.sav")
        clf4 = joblib.load(base + "models/GradientBoostingClassifier.sav")
        clf5 = joblib.load(base + "models/KNeighborsClassifier.sav")
        clf6 = joblib.load(base + "models/GaussianNB.sav")
        clf7 = joblib.load(base + "models/GaussianMixture.sav")

        model_list = [clf1, clf2, clf3, clf4, clf5, clf6, clf7]

        with open(base + "models/rtb.jump", 'rb') as file:

            rtb = pickle.load(file)

        with open(base + "models/labels_dictionary.jump", 'rb') as file:

            labels_dictionary = pickle.load(file)

        ########### getting stream source
        cam = None

        if self.camera_add != "":
            #cam = cv2.VideoCapture('rtsp://admin:admin@192.168.1.152:554')  # cp plus camera
            cam = cv2.VideoCapture(self.camera_add)  # cp plus camera
            
            if cam.isOpened():
                print(" URL camera opened")
            else:
                print("URl for camera is not correct, please check URL : " ,self.camera_add )

        else:
            print("incorrect camera address, hence using laptop webcam")
            cam = cv2.VideoCapture(0)   # laptop camera
            
            if cam.isOpened():
                print("Laptop WebCam opened")
            else:
                print("could open laptop camera too")

        ############

        faceCascade = cv2.CascadeClassifier(cascPath)

        while True:

            ret, frame = cam.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                img,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(32, 32),
            )

            for (x, y, w, h) in faces:

                record = img[y:y + h, x:x + w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 255, 100), 1)
                record = cv2.resize(record, (training_img_size, training_img_size))
                record = np.array(record)
                #print("record shape is ",record.shape)
                ###############################################################

                #record = record.reshape((1, record.shape[0], record[1]))
                record = np.resize(record, (1, record.shape[0]*record.shape[1]))
                record = np.dot(record, rtb)
                predictions_by_childs = list()

                for model, i in zip(model_list, range(len(model_list))):

                    predicted_label = model.predict(record)
                    #print("Model number -> ", i, "Predicted: label", predicted_label)
                    predictions_by_childs.append(predicted_label[0])

                try:

                    predicted_label_final = labels_dictionary[mode(
                        predictions_by_childs)]
                    print(predicted_label_final)
                    cv2.putText(frame, predicted_label_final, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 1,
                                cv2.LINE_AA)

                except Exception as e:

                    print(e)

            cv2.imshow("Prediction Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):

                break



if __name__ == "__main__":

    res = 'y'
    res1 = input("Want predictions? [y/n]: ")
    if res1 == 'y':
        
        j=AI_cam()
        j.start_detection()
        print("webcam started detection")
        k=AI_cam(cam_address="rtsp://admin:admin@192.168.1.152:554")
        k.start_detection()
        print("url cam  started detection")


        
