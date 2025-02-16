import cv2
import numpy as np


img = cv2.imread("F:\\Computer Vision\\Images\\col_balls.jpg",0)

cv2.imshow("image",img)

#EROSION

# At the time of masking background should always be black so use binary or binary inverse according to that 
_,mask = cv2.threshold(img, 230, 255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8) # Structuring element - hover to all the boundaries using this and sharpen the image
e = cv2.erode(mask,kernel)
 

cv2.imshow("erosion",e)
cv2.imshow("mask",mask)


#DIALATION - opposite of erosion

kernel = np.ones((4,4),np.uint8)
d = cv2.dilate(mask,kernel)

cv2.imshow("dialation",d)


cv2.waitKey(0)
cv2.destroyAllWindows()





