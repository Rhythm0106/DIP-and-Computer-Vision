# There are two types of filters - LOW Pass Filter and High Pass Filter 
# Low Pass - Used to remove noise
# High Pass - Used to detect and find edges in an image

import cv2
import numpy as np


img = cv2.imread("F:\\Computer Vision\\Images\\noisy.jpg")
img = cv2.resize(img,(400,400))

cv2.imshow("image",img)


# 1) Homogenous filter or 2 D matrix 

kernel = np.ones((5,5),np.uint32)/25

h_filter = cv2.filter2D(img, -1, kernel)
cv2.imshow("homogenous",h_filter)


# 2) blur

blur = cv2.blur(img,(5,5))
cv2.imshow("blur" ,blur)

# 3) Gaussian Blur filter


gau = cv2.GaussianBlur(img, (5,5), 0) # Sigma x is the spacing of pixel which is 0 currently
cv2.imshow("gaussian", gau)



# 4) Median blur --> Salt and pepper noise ---> white dots on black portion of the image
# Dont take it even otherwise outputs will not be displayed and by default it's value is one


med = cv2.medianBlur(img,5)
cv2.imshow("median blur ",med)



# 5) Bi-lateral filter --> highly effective for noise removal at edges 

bi_f = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("bilateral",bi_f)



cv2.waitKey()
cv2.destroyAllWindows()

