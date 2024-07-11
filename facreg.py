import cv2 
import os

if os.path.exists("detected_face"):
    print("detected_face folder already exists")
else:
    try:
        os.mkdir("detected_face")
    except Exception as e:
        print(e)
        
    print("detected_face folder created ")



font=cv2.FONT_HERSHEY_SIMPLEX

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
a=1
rollno=int(input("enter the rollno : "))
name=input("enter the name : ")
while True:
    check,frame=video.read()
   
    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05, minNeighbors=5,minSize=(70,70))
    
    imageop2=frame
    cropimage=frame
    for x,y,w,h in faces:
        cropimage = imageop2[y + 2:y + h - 2, x + 2:x + w - 2]
        imageop=cv2.rectangle(frame, (x, y), (x+w,y+h), (99, 255, 3), 2)
        imageop2=cv2.putText(imageop, str("detected face"),(x+w//3,y+h+15),font,w/250,(125, 255, 255),2)
        
    resizeimg = cv2.resize(cropimage, (400, 400))
    
    if cropimage is frame:
        pass
    else:
        a+=1
        print(a)
        cv2.imwrite("detected_face/"+name+str('.')+str(rollno) +str('.')+ str(a)+ ".jpg", cropimage)
    
    cv2.imshow("vid", imageop2)
    key=cv2.waitKey(10)
    if key==ord("q") or key==27:
        break
    elif a>=100:
        break
    
video.release()
cv2.destroyAllWindows()
##class change pana poriyaaaa nalla
