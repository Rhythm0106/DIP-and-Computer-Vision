import cv2

img1 = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg",0)
print(img1)
cv2.imshow("original", img1)
cv2.waitKey(3000)
cv2.destroyAllWindows()