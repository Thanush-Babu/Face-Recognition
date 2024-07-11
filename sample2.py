import cv2
from PIL import Image
import os
import numpy as np
def getImagesAndLabels(path):
    imagePaths=[]
    img_names=os.listdir(path)
    for img_name in img_names:
        fullimgpath=os.path.join(path,img_name)
        print(fullimgpath)
        imagePaths.append(fullimgpath)
    print(imagePaths)
    for imagePath in imagePaths:
        img=cv2.imread(imagePath)
        cv2.imshow('pic',img)
        cv2.waitKey(100)
        cv2.destroyAllWindows()
getImagesAndLabels("detected_face")
