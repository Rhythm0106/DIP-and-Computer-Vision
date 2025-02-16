import cv2
import numpy as np

# When we make change in the direction or intensity of the color it is called gradient

img = cv2.imread("F:\\Computer Vision\\Images\\avengers.jpg")

img = cv2.resize(img,(600,500))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplace Transformation

lap = cv2.Laplacian(img, cv2.CV_64F) # it also generate negative value and we can also keep kernel size
lap = np.uint8(np.absolute(lap))

# Sobel X and Sobel Y
 
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize = 3)  # Focuses on vertical lines
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize = 3)  # Focuses on horizontal lines

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_combined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("laplace ", lap)
cv2.imshow("orignal image",img)
cv2.imshow("Combined",sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()