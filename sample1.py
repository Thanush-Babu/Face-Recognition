import cv2
from PIL import Image
import os
import numpy as np
def getImagesAndLabels(path):
    img_names=os.listdir(path)
    for img_name in img_names:
        fullimgpath=path+'/'+img_name 
        print(fullimgpath)
        img=cv2.imread(fullimgpath)
        cv2.imshow('pic',img)
        cv2.waitKey(100)
        cv2.destroyAllWindows()
getImagesAndLabels("detected_face")
