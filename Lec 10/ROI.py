import cv2
import numpy as np

img = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg")
img = cv2.resize(img,(1500,791))

roi = img[93:386,619:886]
#(619,93) (886,386)
img[93:386,874:1141] = roi
img[93:386,1138:1405] = roi
img[93:386,352:619] = roi
img[93:386,85:352] = roi


cv2.imshow("thor", img)
cv2.waitKey(0)
cv2.destroyAllWindows()