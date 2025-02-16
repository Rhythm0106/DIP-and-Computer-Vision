import cv2

img = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")

brdr = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_CONSTANT,value= (252, 3, 61))

cv2.imshow("border tree",brdr)

cv2.waitKey(0)
cv2.destroyAllWindows()
