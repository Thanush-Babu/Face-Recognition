import cv2
from PIL import Image
import os
import numpy as np
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f)for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        img=cv2.imread(imagePath)
        
        cv2.imshow('',img)
        cv2.waitKey(100)
        cv2.destroyAllWindows()
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        print(Id)
        Ids.append(Id)        
    return faces,Ids

def trainimage():
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    
    detector =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces,Id = getImagesAndLabels("detected_face")
    recognizer.train(faces, np.array(Id))
    recognizer.save("dare.yml")


trainimage()
