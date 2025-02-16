# Contours help in shape detection, analyzation and recognition

# for findContour function always have white object in black background 

import cv2
import numpy as np
img = cv2.imread("F:\\Computer Vision\\Images\\logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1, 20, 255, 0) # threshold decides how your contours will be 
# this threshold function means that less than 127 will be black and greater than 127 will be white

cnts,heir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#In this function it will return two things
# 1) A list which will contain coordinates of contours 
# 2) heirarchy

print(cnts,len(cnts)) # this will print a array with its length

img = cv2.drawContours(img,cnts,10,(176,10,15),4) # 4 is thickness other is colour code 
# Here -1 means all parts will be contoured if you give certain number than only that part will be affected

cv2.imshow("orignal", img)
cv2.imshow("threhold",thresh)
cv2.imshow("gray scale", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Decrease the threshold accordingly to the area you want 

"""

Steps :
    
1) Convert to gray scale
2) Calculate threshold


"""