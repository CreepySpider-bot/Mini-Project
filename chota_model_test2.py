import math
import cv2
import numpy as np
from tensorflow import keras
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
offset = 20
imgSize = 300
classes = ["A","B","C","D"]
model = keras.models.load_model('saved_model/my_model_1')
detector = HandDetector(maxHands=1)
res = "-1"

while(True):
    success,img = cap.read()
    hands , img = detector.findHands(img)
    
    if(hands):
        hand = hands[0]
        x,y,w,h = hand['bbox']
        
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset ,x-offset:x+w+offset]
        
        
        aspect_ratio = h/w
        if aspect_ratio>1:
            k = imgSize/h
            wcal = math.ceil(k*w) 
            imgResize = cv2.resize(imgCrop,(wcal,imgSize))
            wGap = math.ceil((imgSize-wcal)/2)
            imgWhite[:,wGap:wcal+wGap] = imgResize
        else:
            k = imgSize/w
            hcal = math.ceil(k*h) 
            imgResize = cv2.resize(imgCrop,(imgSize,hcal))
            hGap = math.ceil((imgSize-hcal)/2)
            imgWhite[hGap:hcal+hGap,:] = imgResize
            
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
        newimg = cv2.resize(imgWhite,(28,28))
        newimg = newimg[np.newaxis,:]
        res = classes[np.argmax(model.predict(newimg))]
        
        print(newimg.shape)
            
    cv2.putText(img,res,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255), 3)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
