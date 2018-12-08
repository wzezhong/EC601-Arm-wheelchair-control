
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pytesseract as pt
import sys

# In[2]:



image = cv2.imread(sys.argv[1])
blur = cv2.GaussianBlur(image,(5,5),0)
gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)  
ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY_INV) 
# cv2.imshow('binaryimage', thresh)
# cv2.imwrite('binaryimage.jpg', thresh)
kernel = np.ones((10,15), np.uint8) 


# In[3]:


#find contours 
#ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_,ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sort contours 
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])


# In[4]:


for i,ctr in enumerate(sorted_ctrs): 
    # Get bounding box 
    x, y, w , h = cv2.boundingRect(ctr)
    if h > 10 and w > 10:
    	M = cv2.moments(ctr)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print("Centroids "+ str(cX)+","+str(cY))
        cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),2)


# In[ ]:


#Show marked areas
cv2.imshow('door',image) 
#Save result
cv2.imwrite('door_result.png',image) 
cv2.waitKey(0)

