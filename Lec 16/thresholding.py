import cv2
import numpy as np

image = cv2.imread("F:\\Computer Vision\\Images\\black_white.png",0)
image = cv2.resize(image,(300,300))

_,th1 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)


cv2.imshow("original",image)
cv2.imshow("Thresh Binary",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()