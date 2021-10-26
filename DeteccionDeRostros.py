# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:11:46 2021

@author: USER
"""

import cv2

#namedWindow("webcam")
# cap = cv2.VideoCapture(0);

# while True:
#     ret , frame = cap.read()
#     cv2.imshow("webcam", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break;
# cap.release()
# cv2.destroyAllWindows()
       

#cv2.faces.LBPHFaceRecognizer_create



def recognize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    isIdentifyed = False

    font = cv2.FONT_HERSHEY_COMPLEX

    cap = cv2.VideoCapture(0);
    
    Id = 0
    conf = 100
    x = 0
    y = 0
    h = 0

    while True:
        ret , frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
      
        for (x, y, w, h) in faces:
            cv2.rectangle(frame,(x, y),(x+w, y+h),(225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        
        if (conf<50):
            if (Id==1):
                Id="Edwin"
                isIdentifyed = True
                
        else:
            Id="Buscando..."
            
        if ( len(faces) > 0):
            cv2.putText(frame,str(Id), org=(x,y+h),fontFace=font, fontScale=2 , color=(0,0,0)  ) 
            
            
        #if isIdentifyed:break
        cv2.imshow("Resultado", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

      #eval_js('showimg("{}")'.format(image2byte(im)))
      #if isIdentifyed:break
    cap.release()
    cv2.destroyAllWindows()

    #return conf
    return isIdentifyed

x = recognize()

 


