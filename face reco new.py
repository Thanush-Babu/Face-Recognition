import cv2
from PIL import Image
import os
import numpy as np


def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("dare.yml")
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    tt='' 
    while True:
        ret,im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            
            conf=int(conf)
            Id=int(Id)
            print(Id, conf)
            if(30< conf <90):
                
              
                if Id==29:
                    nam='thanush'
                    tt=str(Id)+"-"+nam    
                elif Id==49:
                    nam='latthika'
                    tt=str(Id)+"-"+nam
                
                else:
                    tt='unknown'
                    
                
             
            elif(conf>90 or conf<30):
                Id='Unknown'                
                tt=str(Id)
                
                    
            
            cv2.putText(im,str(tt),(x,y+h), font, w/250,(255,255,255),2)        
                    
        cv2.imshow('image Detected',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
            
    cam.release()
    cv2.destroyAllWindows()

TrackImages()



