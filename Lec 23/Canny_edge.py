import cv2
import numpy as np

img = cv2.imread("F:\\Computer Vision\\Images\\building.jpg")
img = cv2.resize(img,(600,600))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""
canny = cv2.Canny(img_gray,50,150) #This threshold is not fixed it varies according to image

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("canny==",canny)

# So as threshold varies we will put a trackbar 

cv2.waitkey()
"""

def nothing():
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)


while True:
    a = cv2.getTrackbarPos("Threshold", "Canny")        
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny", res)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()