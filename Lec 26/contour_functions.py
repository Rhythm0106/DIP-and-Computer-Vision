# Contour functions
# 1) Moment   2) Approximation  3) ConvexHull


import cv2
import numpy as np


img = cv2.imread("F:\\Computer Vision\\Images\\shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,200, 255,cv2.THRESH_BINARY_INV)

# Now to find contour 

cnts,hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours are" , cnts, "\ntotal contours =", len(cnts))

# If you want to find centre or weighted mask then moment function is used 

# Now looping over the cotours for moment function 

for c in cnts:
    M = cv2.moments(c)
    print("M==", M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv2.drawContours(img, [c], -1, (0,255,0),2)


# img = cv2.drawContours(img, cnts, -1, (10,20,100),4)

cv2.imshow("orignal", img)
cv2.imshow("threhold",thresh)
cv2.imshow("gray scale", img1)


cv2.waitKey(0)
cv2.destroyAllWindows()




    