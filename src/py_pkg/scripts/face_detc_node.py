#!/usr/bin/env python3
#coding=UTF-8

#import libraries
import cv2
import numpy as np
#import 


HAAR_CASCADE_XML_FILE_FACE='/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
GSTREAMER_PIPELINE='nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'

def faceDetect():
    face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_XML_FILE_FACE)
    video_capture = cv2.VideoCapture(0)
    if video_capture.isOpened():
        cv2.namedWindow("Face Detection Window",cv2.WINDOW_AUTOSIZE)

        while True:
            return_key, image = video_capture.read()
            if not return_key:
                break

            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            detected_faces = face_cascade.detectMultiScale(grayscale_image,1.3,5)

            for(x_pos,y_pos,width,height) in detected_faces:
                cv2.rectangle(image,(x_pos,y_pos),(x_pos+width,y_pos+height),(255,0,255),2)
            
            cv2.imshow("Face Detection Window",image)

            key = cv2.waitKey(30) & 0xff

            if key==27:
                break
        
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Cannot open Camera")


if __name__ == "__main__":
    faceDetect()









