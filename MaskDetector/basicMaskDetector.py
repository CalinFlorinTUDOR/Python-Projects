import cv2
import os
import face_recognition


capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

counter = 0

while True:
  success, img = capture.read()
  
  faceDetector = face_recognition.face_locations(img)
  
  if faceDetector:
    counter = 0
    cv2.putText( img, 'Access denied!', (150, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
    cv2.putText( img, 'Mask undetected!', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
    
  else:
    counter += 1
    if counter > 20:
        cv2.putText( img, 'Authorized access!', (150, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
        cv2.putText( img, 'Mask detected!', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)
  
  
  cv2.imshow('Mask Detector', img)
  cv2.waitKey(1)