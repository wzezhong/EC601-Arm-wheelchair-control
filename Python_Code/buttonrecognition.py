import sys
import argparse
import cv2
import numpy as np
import pytesseract as pt
import os


def create_dir(dir_name):
  #Make an Image directory to save frames from video
  if not os.path.exists(dir_name):
    os.makedirs(dir_name)
  else:
    #If directory exists, clear its contents to save the frames
    folder = dir_name
    for the_file in os.listdir(folder):
      file_path = os.path.join(folder, the_file)
      try:
        if os.path.isfile(file_path):
          os.unlink(file_path)
      except Exception as e:
        print(e)

def detectCircle(circleImage):
  cimg = cv2.cvtColor(circleImage,cv2.COLOR_BGR2GRAY)
  #cv2.imwrite("grey.jpg",cimg)
  circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,100,
                              param1=50,param2=30,minRadius=3,maxRadius=20)
  if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:
          # draw the outer circle
          cv2.circle(circleImage,(i[0],i[1]),i[2],(0,255,0),2)
          # draw the center of the circle
          cv2.circle(circleImage,(i[0],i[1]),2,(0,0,255),3)
  return circleImage

def detectNumber(image,numtodetect,pathOut):
  blur = cv2.GaussianBlur(image,(5,5),0)
  gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)  
  ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY_INV) 
  #cv2.imwrite("bw.jpg",thresh)
  kernel = np.ones((10,15), np.uint8)

  #Find contours 
  _,ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  #sort contours 
  sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

  for i,ctr in enumerate(sorted_ctrs): 
      # Get bounding box 
      x, y, w, h = cv2.boundingRect(ctr) 

    # Getting ROI 
      if w > 5 and h > 5:
        #Make ROI smaller than bounding box to remove edges
        mx1 = (x + x + w)/2
        mx2 = (x + mx1)/2
        mx3 = (x +mx2)/2
        height = mx2 - x
        my1 = (y + y + h)/2
        my2 = (y + my1)/2
        my3 = (y+my2)/2
        my4 = (y+my3)/2
        width2 = my3 - y
        width1 = my4 - y
        roi = thresh[y+width1:y+h-width2, x+height:x+w-height]
        num = pt.image_to_string(roi, config="--psm 13, outputbase digits")
        cv2.imwrite("roi/numl"+num+'.png'.format(i), roi)
        if len(num) > 1:
          continue
        elif(num == numtodetect):
          print("Detected "+numtodetect)
          M = cv2.moments(ctr)
          cX = int(M["m10"] / M["m00"])
          cY = int(M["m01"] / M["m00"])
          print("Centroids "+ str(cX)+","+str(cY))
          cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),2)
          cv2.circle(image, (cX, cY), 2, (255, 255, 255), -1) 
          cv2.putText(image, str(num), (x,y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
        else:
          continue
  return image


def convert_images_to_video(dir_name):
  #Using ffmpeg to convert images to video.
  os.system("ffmpeg -loglevel panic -r 1/2 -i "+dir_name+"/frame%d.jpg -vcodec mpeg4 -y "+"detected_video"+".mp4")
  create_dir("circles")
  for the_file in os.listdir("circles"):
      file_path = os.path.join("circles", the_file)
      try:
        if os.path.isfile(file_path):
          os.unlink(file_path)
      except Exception as e:
        print(e)
  os.system("ffmpeg -loglevel panic -r 1/2 -i circles/cir%d.jpg -vcodec mpeg4 -y "+"circle"+".mp4")


def extractImages(pathIn, pathOut, number):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
      success,image = vidcap.read()
      ## Stop when last frame is identified
      image_last = cv2.imread("frame{}.png".format(count-1))
      if np.array_equal(image,image_last):
          break
      print ('Read a new frame: ', success)
      circleImage = image.copy()
      imagefinal = detectNumber(image,number,pathOut)
      cv2.imwrite( pathOut + "frame%d.jpg" % count, imagefinal)     # save frame as JPEG file
      cir = detectCircle(circleImage)
      count += 1
      cv2.imwrite( "circles/" + "cir%d.jpg" % count, cir)
    convert_images_to_video(pathOut)
    

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    a.add_argument("--number", help="number to detect")
    args = a.parse_args()
    print(args)
    create_dir(args.pathOut)
    extractImages(args.pathIn, args.pathOut, args.number)
