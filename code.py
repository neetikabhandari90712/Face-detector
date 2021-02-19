pip install opencv-python
import cv2
# from google.colab.patches import cv2_imshow
from random import randrange
#Load some pre trained data on face frontals from opencv (haarcascade alogorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Choose an image to detect the faces in 
# img = cv2.imread('RDJ.png')
webcam = cv2.VideoCapture(0)

while True:
    sucessful_frame_read, frame = webcam.read()
    
      # must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    # print(face_coordinates)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x, y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)
    cv2.imshow('Made by a smart programmer',frame)
    cv2.waitKey(1)
    
    #Stop if Q key is pressed
    if key==81 or key == 113:
        break

