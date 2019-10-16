#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2

#make a Cascade classifier object
face_cascade = cv2.CascadeClassifier("C:\\Users\\geetk\\Downloads\\opencv2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml")

#Capture image from camera
cap = cv2.VideoCapture(0)

while 1:
    ret,img = cap.read()
    #reading the image as gray scale image
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #search the co-ordinates of the image
    faces = face_cascade.detectMultiScale(gray_image,scaleFactor = 1.05,minNeighbors = 5)

    #building a rectangle for a face
    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y) ,(x+w, y+h),(0,255,0),3)


    cv2.imshow("img",img)
    
    
    #press ESC key to get out of the while loop
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release()

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




