import cv2
import numpy as np 

img = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg")
img = cv2.resize(img,(700,700))

img = cv2.line(img,(0,0) ,(200,200),(168, 50, 52),1)
cv2.imshow("drawing",img)
cv2.waitKey(0) 
cv2.destroyAllWindows()