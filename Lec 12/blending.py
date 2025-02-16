import cv2 
import  numpy as np

img1 = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")
img1 = cv2.resize(img1,(700,700))
img2 = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg")
img2 = cv2.resize(img2,(700,700))

#cv2.imshow("img1", img1)
#cv2.imshow("img2",img2)


#result = img2 + img1
result1 = cv2.add(img1,img2)

result2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("result1", result1)
cv2.imshow("result2",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

