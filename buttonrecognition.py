#import libraries
import cv2
import numpy as np
import pytesseract as pt
import sys


#Read image passed as argument
im = sys.argv[1]
numtodetect = sys.argv[2]
image = cv2.imread(im)

#Image Processing
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
#cv2.imshow('gray', gray) 
#cv2.waitKey(0) 
#binary 
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV) 
#cv2.imshow('second', thresh) 
#cv2.waitKey(0) 
kernel = np.ones((10,15), np.uint8) 


#Find contours for button recognition 
#ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_,ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sort contours 
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])


#Add bounding rectangles and detect numbers
for i,ctr in enumerate(sorted_ctrs): 
    # Get bounding box 
    x, y, w, h = cv2.boundingRect(ctr) 
    
    # Getting ROI 
    if w > 50 and h > 50:
        if h > w:
            my1 = (y + y + h)/2
            my2 = (y + my1)/2
            my3 = (y+my2)/2
            width = my2 - y
            mx1 = (x + x + w)/2
            mx2 = (x + mx1)/2
            mx3 = (x +mx2)/2
            height = mx2 - x
            roi = thresh[y+width:y+h-width, x+height:x+w-height]
        else:
            roi = thresh[y:y+h, x:x+h]
        # if cv2.countNonZero(roi) < 5000:
        #     continue
        #cv2.imshow('roi',roi)
        cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),2) 
        num = pt.image_to_string(roi, config="--psm 13, outputbase digits")
        if len(num) > 1:
            continue
        elif(num == numtodetect):
            cv2.putText(image, str(num), (x,y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
        else:
            continue
        #cv2.imwrite("num"+num+'.png'.format(i), roi)
        #cv2.putText(image, str(num), (x,y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)


#Show marked areas
cv2.imshow('marked areas',image) 
#Save result
cv2.imwrite('result.png',image) 
cv2.waitKey(0)

