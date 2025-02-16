# Multiple resolutions of a single image  -- used to find object or do blending 

import cv2
import numpy as np 

"""
img = cv2.imread("F:\\Computer Vision\\Images\\avengers.jpg")
img = cv2.resize(img, (600,600))


# Gaussian pyramid --->  pyrdown()

pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)




cv2.imshow("pyramid down",pd1)
cv2.imshow("image",img)
"""




# Doing using for loop

img = cv2.imread("F:\\Computer Vision\\Images\\avengers.jpg")
img = cv2.resize(img, (600,600))

img1 = img.copy()

data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+ str(i),img1)


cv2.waitKey(0)
cv2.destroyAllWindows()

